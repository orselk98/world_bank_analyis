import pandas as pd
import os
print(os.getcwd())



def inspect_data(df):
    print("Shape:",df.shape)

    print("\nColumns Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print(df.head())

    df=df.drop("Unnamed: 70", axis=1)
    print("Shape:",df.shape)


if __name__=="__main__":
    df=pd.read_csv("data/raw/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_107.csv", skiprows=4)
    inspect_data(df)