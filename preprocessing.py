from data.raw_data import fetch_api
import pandas as pd

#fetch data
data = fetch_api()

# data
df = pd.DataFrame(data['data'])

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

    #round float cols
    new_col = df.columns.drop(['split_factor','dividend','symbol', 'exchange', 'date', 'month' , 'year'])
    for col in new_col:
        df[col] = df[col].round()

    return(df)
   
def run_preprocessing_pipeline(df):
    
    df = preprocess(df)
    df.to_csv("data/new_data.csv",index = False)
    return df



