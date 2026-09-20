import numpy as np
import pandas as pd

def add_moving_averages(df: pd.DataFrame, sma_short: int, sma_long: int, sma_macro: int, epsilon: float | int) -> pd.DataFrame:
    close = df["close"]
    short_sma_name = f"SMA_{sma_short}"
    long_sma_name = f"SMA_{sma_long}"
    macro_sma_name = f"SMA_{sma_macro}"

    df[short_sma_name] = close.rolling(window=sma_short, min_periods=sma_short).mean()
    df[long_sma_name] = close.rolling(window=sma_long, min_periods=sma_long).mean()
    df[macro_sma_name] = close.rolling(window=sma_macro, min_periods=sma_macro).mean()
    df["SMA_Ratio"] = df[short_sma_name] / (df[long_sma_name] + epsilon)
    trend_conditions = [
        close > df[macro_sma_name],
        close < df[macro_sma_name],
        close == df[macro_sma_name]
    ]
    trend_values = [1, -1, 0]
    df["Macro_Trend"] = np.select(trend_conditions, trend_values, default=np.nan)

    return df