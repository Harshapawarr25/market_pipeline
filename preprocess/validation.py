import json
import pandas as pd


def validate_data(df):

    required_columns = [
        "open", "high", "low", "close",
        "volume", "date", "symbol"
    ]

    validation_output = {

        # check duplicate rows
        
        "duplicate_rows": int(
            df.duplicated().sum()
        ),

        # validate negative value

        "negative_open_prices": int(
            (df["open"] < 0).sum()
        ),

        "negative_close_prices": int(
            (df["close"] < 0).sum()
        ),

        "negative_high_prices": int(
            (df["high"] < 0).sum()
        ),

        "negative_low_prices": int(
            (df["low"] < 0).sum()
        ),

        # validate volume
        "negative_volume": int(
            (df["volume"] < 0).sum()
        ),

        # validate date format
        "invalid_dates": int(
            pd.to_datetime(
                df["date"],
                errors="coerce"
            ).isnull().sum()
        ),

        # datatype validation
        "data_types": (
            df.dtypes
            .astype(str)
            .to_dict()
        )
    }

    # save validation report
    with open("exports/validation_report.json", "w") as file:
        json.dump(validation_output, file, indent=4)

    print("Data validation completed successfully")

    return df


def run_validation_pipeline():

    df = pd.read_csv("data/raw_data.csv")

    df = validate_data(df)

    return df

