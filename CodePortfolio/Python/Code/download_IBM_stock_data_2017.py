import pandas as pd
from pandas_datareader import data as web
df = web.DataReader("IBM", 'yahoo', '1/1/2017', '1/31/2017')
df.columns.values
df = df.drop(['Adj Close'], axis = 1)
df.to_csv("../Data/ibm.csv")