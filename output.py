import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Barchart of closing price vs date
def plot_close_price(df):

    plt.figure(figsize=(8,5))
    sns.lineplot(x="date", y="close", data=df) 
    plt.title("closing price data")
    plt.xticks(ticks=df.index[::10],labels=df["date"][::10],rotation=45,fontsize=7, )
    plt.savefig("charts/closing_price_chart.png")
    plt.show() 

#linechart of opening price vs date
def plot_open_price(df):

    plt.figure(figsize=(8,5))
    sns.lineplot(x="date", y="open", data=df) 
    plt.title("Opening price data")
    plt.xticks(ticks=df.index[::10],labels=df["date"][::10],rotation=45,fontsize=7, )
    plt.savefig("charts/Opening_price_chart.png")
    plt.show() 


def trading_volume(df):
    plt.figure(figsize=(12,5))
    plt.bar(df.index, df["volume"])
    plt.title("Trading volume")
    plt.xticks(ticks=df.index[::10],labels=df["date"][::10],rotation=45)
    plt.savefig("charts/Trading_volume_chart.png")
    plt.show()

#heat map
def heat_map(df):
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True,fmt=".2f",cmap="coolwarm")
    plt.title("Heatmap")
    plt.savefig("charts/stock_chart.png")
    plt.show()

def run_output_file():

    df = pd.read_csv("data/featured_data.csv")
    plot_close_price(df)
    plot_open_price(df)
    trading_volume(df)
    heat_map(df)
    return df
