import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Barchart of closing price vs date
def plot_close_price(df):

    plt.figure(figsize=(8,5))
    sns.lineplot(x="date", y="close", data=df) 
    plt.title("closing price data")
    plt.xticks(ticks=df.index[::10],labels=df["date"][::10],rotation=45,fontsize=6 )
    plt.savefig("visualization/closing_price_chart.png")
    try:
        plt.savefig("visualization/closing_price_chart.png")
        print("Closing price chart saved successfully")
    except Exception as error:
        print("Error while saving chart")
    
    

#linechart of opening price vs date
def plot_open_price(df):

    plt.figure(figsize=(8,5))
    sns.lineplot(x="date", y="open", data=df) 
    plt.title("Opening price data")
    plt.xticks(ticks=df.index[::10],labels=df["date"][::10],rotation=45,fontsize=6 )
    plt.savefig("visualization/Opening_price_chart.png")
    try:
        plt.savefig("visualization/Opening_price_chart.png")
        print("Opening price chart saved successfully")
    except Exception as error:
        print("Error while saving chart")
    


def trading_volume(df):
    plt.figure(figsize=(12,5))
    plt.bar(df.index, df["volume"])
    plt.title("Trading volume")
    plt.xticks(ticks=df.index[::10],labels=df["date"][::10],rotation=45,fontsize = 6 )
    plt.savefig("visualization/Trading_volume_chart.png")
    try:
        plt.savefig("visualization/Trading_volume_chart.png")
        print("Trading volume chart saved successfully")
    except Exception as error:
        print("Error while saving chart")
    

#heat map
def heat_map(df):
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True,fmt=".2f",cmap="coolwarm")
    plt.title("Heatmap")
    plt.savefig("visualization/stock_chart.png")
    try:
        plt.savefig("visualization/stock_chart.png")
        print("Heatmap saved successfully")
    except Exception as error:
        print("Error while saving chart")
  

def run_output_file():

    df = pd.read_csv("data/featured_data.csv")
    print("Saving chart visualizations...")
    plot_close_price(df)
    plot_open_price(df)
    trading_volume(df)
    heat_map(df)
    return df

run_output_file()
