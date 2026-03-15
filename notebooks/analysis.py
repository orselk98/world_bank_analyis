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
    
    print("\nNumber of NAN values in cleaned DataFrame:")
    print(cleaned_df.isnull().sum())


def clean_data(df):
    df=df.drop("Unnamed: 70", axis=1)
    year_columns=[str(year) for year in range(1990,2024)]
    df=df[["Country Name","Country Code","Indicator Name","Indicator Code"]+year_columns]
    return df

    #Nan strategy: leave as it is - Missing GDP data is intentional
    #(there are non reporting countries). pandas aggregations skip NaNs by default.



if __name__=="__main__":
    df=pd.read_csv("data/raw/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_107.csv", skiprows=4)
    inspect_data(df)
    cleaned_df=clean_data(df)
    print("\nCleaned DataFrame shape:",cleaned_df.shape)