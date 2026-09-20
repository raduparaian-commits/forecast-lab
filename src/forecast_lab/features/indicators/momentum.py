import pandas as pd

def add_returns(df: pd.DataFrame, return_periods: list[int]) -> pd.DataFrame:
    for period in return_periods:
        df[f"Return_{period}m"] = df["close"].pct_change(periods=period, fill_method=None)

    return df

def add_rsi(df: pd.DataFrame, rsi_period: int, epsilon: float | int) -> pd.DataFrame:
    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    average_gain = gain.ewm(alpha=1 / rsi_period, adjust=False, min_periods=rsi_period).mean()
    average_loss = loss.ewm(alpha=1 / rsi_period, adjust=False, min_periods=rsi_period).mean()
    relative_strength = average_gain / (average_loss + epsilon)
    rsi = 100 - (100 / (1 + relative_strength))
    rsi = rsi.mask((average_loss == 0) & (average_gain > 0), 100)
    rsi = rsi.mask((average_gain == 0) & (average_loss > 0), 0)
    rsi = rsi.mask((average_gain == 0) & (average_loss == 0), 50)
    df[f"RSI_{rsi_period}"] = rsi

    return df