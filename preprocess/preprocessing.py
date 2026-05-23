import pandas as pd
import os


#data from csv
df = pd.read_csv("data/raw_data.csv")

def preprocess(df):
    # split month 
    df['month'] = df['date'].str.split("-").str[1] # 04,05
    
    # Split year
    df['year'] = df['date'].str.split("-").str[0] # 2020


    # Convert date format
    formatted_date = df['date'].str.split("T").str[0]  # 2026-05-11
    parts = formatted_date.str.split("-")
    df['date'] = (
        parts.str[2] + "-" +
        parts.str[1] + "-" +
        parts.str[0]
    )

    # rounding numerical columns
    new_col = df.columns.drop(['split_factor','dividend','symbol', 'exchange', 'date', 'month' , 'year'])
    for col in new_col:
        df[col] = df[col].round()
    
    return(df)
   
def run_preprocessing_pipeline(df):
    
    df = preprocess(df)
    print("Data preprocessing pipeline started..")
    try:
        df.to_csv("data/new_data.csv",index = False)

        if os.path.exists("data/new_data.csv"):
            print("Data cleaning process completed successfully. Output saved as 'new_data.csv'")
    except Exception as error:
        print(f"Error while saving file: {error}")

    
    return df
