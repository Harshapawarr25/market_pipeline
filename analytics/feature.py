import pandas as pd
import os

df = pd.read_csv("data/new_data.csv")

def feature_data(df):

   df =  df.drop(['split_factor','dividend','symbol','exchange','adj_open','adj_low','adj_close','adj_high'],axis= 1)
   try :
      df.to_csv("data/featured_data.csv")
      if os.path.exists("data/featured_data.csv"):
         print("Feature engineering process completed")
      
   except Exception as error:
      print(f"Error while saving file: {error}")

   return df
