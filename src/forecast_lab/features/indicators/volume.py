import pandas as pd

def add_volume_indicators(df: pd.DataFrame, volume_sma_period: int, epsilon: float | int) -> pd.DataFrame:
    volume_sma_name = f"Volume_SMA_{volume_sma_period}"
    df[volume_sma_name] = df["volume"].rolling(window=volume_sma_period, min_periods=volume_sma_period).mean()
    df["Volume_Spike"] = df["volume"] / (df[volume_sma_name] + epsilon)

    return df