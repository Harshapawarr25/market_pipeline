from data.raw_data import fetch_api
import pandas as pd

#fetch data
data = fetch_api()

#view data
df = pd.DataFrame(data['data'])
def view_data(): 
    print("Market stock data:")
    print(df.head(6)) # First six dataset
    print("Generate summary statistics:")
    print(df.describe()) #summary statistics
    return df

#clean data
def analyze_data(df):
    print("counting unique values for each features: ") 
    print(df.nunique())
    #find percentage of missing value
    print("total missing values for each field: ") 
    print(df.isnull().sum())
    print("missings values in perc:\n")
    print((df.isnull().sum() / len(df)) * 100)
    return df


def run_clean_pipeline():
    df = view_data()
    df = analyze_data(df)
    return df

#missing value is zero hence data is already cleaned


