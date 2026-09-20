import pandas as pd

def add_atr_indicators(df: pd.DataFrame, atr_period: int, epsilon: float | int) -> pd.DataFrame:
    high = df["high"]
    low = df["low"]
    close = df["close"]
    previous_close = close.shift(1)
    true_range = pd.concat([high - low, (high - previous_close).abs(), (low - previous_close).abs()], axis=1)
    true_range = true_range.max(axis=1)
    atr = true_range.ewm(alpha=1 / atr_period, adjust=False, min_periods=atr_period).mean()
    atr_sma = atr.rolling(window=atr_period, min_periods=atr_period).mean()

    df["High_Low_Spread"] = (high - low) / (close + epsilon)
    df["True_Range"] = true_range
    df[f"ATR_{atr_period}"] = atr
    df["ATR_Percent"] = atr / (close + epsilon)
    df["ATR_SMA"] = atr_sma
    df["Volatility_Ratio"] = atr / (atr_sma + epsilon)

    return df