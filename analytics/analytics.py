import json
import pandas as pd


def analyze_data(df):

    analytics_output = {

        "market_stock_data": (
            df.head(6)
            .to_dict()
        ),

        "summary_statistics": (
            df.describe(include='all')
            .fillna(0)
            .to_dict()
        ),
    

        "unique_values": (
            df.nunique() 
            .to_dict() # series to dictionary format
        ),

        "missing_values": (
            df.isnull()
            .sum()
            .to_dict() 
        ),

        "missing_percentage": (
            (
                df.isnull().sum() / len(df)
            ) * 100
        ).to_dict()
    }
# save in json format
    with open("exports/analysis_data.json", "w") as file:
        json.dump(analytics_output, file, indent=4)
        print("data is analysed and cleaned sucssesfully")
    

    return df


def run_clean_pipeline():
    
    df = pd.read_csv("data/raw_data.csv")
    df = analyze_data(df)

    return df






