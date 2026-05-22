import pandas as pd

df = pd.read_csv("data/new_data.csv")

def feature_data(df):

   columns =  df.drop(['split_factor','dividend','symbol','exchange','adj_open','adj_low','adj_close','adj_high'],axis= 1)
   columns.to_csv("data/featured_data.csv")

