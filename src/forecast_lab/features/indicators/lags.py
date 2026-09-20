import pandas as pd

def add_lagged_features(df: pd.DataFrame, lag_period: int) -> pd.DataFrame:
    df[f"SMA_Ratio_Lag_{lag_period}"] = df["SMA_Ratio"].shift(lag_period)
    df[f"High_Low_Spread_Lag_{lag_period}"] = df["High_Low_Spread"].shift(lag_period)
    df[f"Volume_Spike_Lag_{lag_period}"] = df["Volume_Spike"].shift(lag_period)

    return df