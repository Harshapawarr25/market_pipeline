import requests 
from dotenv import load_dotenv
import os



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



