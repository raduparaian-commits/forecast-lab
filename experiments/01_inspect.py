import pandas as pd

CSV_PATH = "data/raw/btc_usd_1min.csv"

df = pd.read_csv(CSV_PATH)

print(f"Shape: {df.shape}")
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nData types:")
print(df.dtypes)