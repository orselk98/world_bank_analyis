import pandas as pd
import os
print(os.getcwd())



def inspect_data(df):
    #How big is the dataset?
    print("Shape:",df.shape)
    #shape returns (rows,columns) as a tuple

    #What coulmns do we have?
    print("\nColumns Names:")
    print(df.columns.tolist())

    #What datatype is each column?
    print("\nData Types:")
    print(df.dtypes)

    #What does the data look like?
    print(df.head())

    #How many NAN values do we have?
    print("\nNumber of NAN values in each column:")
    print(df.isnull().sum())

    print("\nDataset Info:")
    print(df.info())



print("--"*50)

def inspect_metadata(metadata_df):
    print("Metadata Shape:",metadata_df.shape)
    print("\nMetadata Column Names:")
    print(metadata_df.columns.tolist())
    print("\nMetadata Data Types:")
    print(metadata_df.dtypes)
    print("\nMetadata Sample:")
    print(metadata_df.head())

print("--"*50)

def clean_data(df):
    #Nan strategy: leave as it is - Missing GDP data is intentional
    #(there are non reporting countries). pandas aggregations skip NaNs by default.
    df=df.drop("Unnamed: 70", axis=1)
    year_columns=[str(year) for year in range(1990,2024)]
    df=df[["Country Name","Country Code",]+year_columns]
    return df

def merge_data(df, metadata_df):
    merged_df=pd.merge(df, metadata_df, on="Country Code", how="left")

    drop_columns=["SpecialNotes","TableName","Unnamed: 5"]
    merged_df=merged_df.drop(columns=drop_columns, errors='ignore')
    return merged_df

def melt_data(merged_df):
    df_melted=merged_df.melt(
        id_vars=["Country Name","Country Code","Region","IncomeGroup"],
        var_name="Year",
        value_name="GDP Growth Rate"
    )
    df_melted["Year"]=df_melted["Year"].astype(int)
    return df_melted

def analyze_data(df):
    #What is the mean GDP growth rate by region?
    mean_gdp_by_region=df.groupby("Region")["GDP Growth Rate"].mean()
    print("\nMean GDP Growth Rate by Region:")
    print(mean_gdp_by_region)

    #How did each region's GDP growth change around 2008 financial crisis?
    start_year=2000
    end_year=2007
    gdp_before_crisis=df[df["Year"].between(start_year, end_year)].groupby("Region")["GDP Growth Rate"].mean().sort_values(ascending=False)
    print(f"\nMean GDP Growth Rate by Region from {start_year} to {end_year}:")
    print(gdp_before_crisis)

    start_year=2008
    end_year=2010
    gdp_after_crisis=df[df["Year"].between(start_year,end_year)].groupby("Region")["GDP Growth Rate"].mean().sort_values(ascending=False)
    print(f"\nMean GDP Growth Rate by Region from {start_year} to {end_year}:")
    print(gdp_after_crisis)

    crisis_analysis=pd.DataFrame({
        "Before Crisis": gdp_before_crisis,
        "After Crisis": gdp_after_crisis,
        "Difference": gdp_after_crisis - gdp_before_crisis
    })
    print("\nGDP Growth Rate Before and After 2008 Crisis:")
    print(crisis_analysis)

    print("\nMean GDP Growth Rate by Income Group:")
    print(df.groupby("IncomeGroup")["GDP Growth Rate"].mean().sort_values(ascending=False))

    filter_nan_values=df[df["Region"].notna() & df["IncomeGroup"].notna() & df["GDP Growth Rate"].notna()]


    print("--"*50)

    print("\nBest and Worst Performing Countries overall:")
    mean_gdp_by_country=filter_nan_values.groupby("Country Name")['GDP Growth Rate'].mean().sort_values(ascending=False)
    print(mean_gdp_by_country.head(10))
    print(mean_gdp_by_country.tail(10))
    



if __name__=="__main__":
    df=pd.read_csv("data/raw/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_107.csv", skiprows=4)
    metadata_df=pd.read_csv("data/raw/Metadata_Country_API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_107.csv")
    #inspect_data(df)

    cleaned_df=clean_data(df)
    #inspect_data(cleaned_df)
    
    #inspect_metadata(metadata_df)
    
    merged_df=merge_data(cleaned_df, metadata_df)
    #inspect_data(merged_df)

    melted_df=melt_data(merged_df)
    #inspect_data(melted_df)
    print(melted_df.shape)
    print(melted_df.head(10))

    #data analysis
    analyze_data(melted_df)