import requests 
from dotenv import load_dotenv
import os
import pandas as pd



load_dotenv()
api_key = os.getenv("api_key")
api_url = f'http://api.marketstack.com/v1/eod?access_key={api_key}&symbols=AAPL'



def fetch_api():
    print("fetching data...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response recives successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occured:{e}")
        raise

def raw_data():
    # fetch api data
    data = fetch_api()

    df = pd.DataFrame(data['data'])

    # save raw dataset snapshot
    df.to_csv("data/raw_data.csv", index=False)

    print("CSV file saved successfully")

    return df

#to fetch api data and convert into csv sheet
raw_data()


