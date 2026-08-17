import pandas as pd

def standardize_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Timestamp"] = pd.to_datetime(df["Timestamp"], unit="s")

    df = df.sort_values(by="Timestamp", ascending=True)

    df = df.set_index("Timestamp")

    return df