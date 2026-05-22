import json
import pandas as pd


def view_data(df):

    view_output = {

        "market_stock_data": (
            df.head(6)
            .to_dict()
        ),

        "summary_statistics": (
            df.describe(include='all')
            .fillna(0)
            .to_dict()
        )
    }

    print(
        json.dumps(
            view_output,
            indent=4,
            default=str
        )
    )

    return df


def analyze_data(df):

    analytics_output = {

        "unique_values": (
            df.nunique()
            .to_dict()
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

    print(
        json.dumps(
            analytics_output,
            indent=4
        )
    )

    return df


def run_clean_pipeline():
    
    df = pd.read_csv("data/raw_data.csv")
    df = view_data(df)
    df = analyze_data(df)

    return df





#missing value is zero hence data is already cleaned


