import pandas as pd

df = pd.read_csv(
    "../data/interim/binance/BTCUSDT/BTCUSDT-1m-2020-01.csv"
)

print(df.head())
print(df.columns)
print(df.shape)