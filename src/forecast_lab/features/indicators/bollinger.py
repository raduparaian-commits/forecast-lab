import pandas as pd

def add_bollinger_bands(df: pd.DataFrame, bb_period: int, bb_std: float | int, epsilon: float | int) -> pd.DataFrame:
    middle_band = df["close"].rolling(window=bb_period, min_periods=bb_period).mean()
    rolling_std = df["close"].rolling(window=bb_period, min_periods=bb_period).std()
    upper_band = middle_band + (rolling_std * bb_std)
    lower_band = middle_band - (rolling_std * bb_std)

    df["Bollinger_Middle"] = middle_band
    df["Bollinger_Upper"] = upper_band
    df["Bollinger_Lower"] = lower_band
    df["Bollinger_Percent_B"] = (df["close"] - lower_band) / (upper_band - lower_band + epsilon)

    return df