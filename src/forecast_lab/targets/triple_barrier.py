import numpy as np
import pandas as pd

def add_triple_barrier_labels(df: pd.DataFrame, horizon_bars: int, take_profit_pct: float | int, stop_loss_pct: float | int, same_bar_policy: str = "stop_loss") -> pd.DataFrame:
    if horizon_bars <= 0:
        raise ValueError("horizon_bars must be greater than zero")

    if take_profit_pct <= 0 or stop_loss_pct <= 0:
        raise ValueError("take_profit_pct and stop_loss_pct must be greater than zero")

    valid_policies = {"stop_loss", "take_profit", "neutral"}

    if same_bar_policy not in valid_policies:
        raise ValueError(f"same_bar_policy must be one of {sorted(valid_policies)}")

    high_prices = df["high"].to_numpy()
    low_prices = df["low"].to_numpy()
    close_prices = df["close"].to_numpy()
    labels = np.full(len(df), np.nan)

    for index in range(max(0, len(df) - horizon_bars)):
        entry_price = close_prices[index]
        upper_barrier = entry_price * (1 + take_profit_pct)
        lower_barrier = entry_price * (1 - stop_loss_pct)
        labels[index] = 0

        future_highs = high_prices[index + 1 : index + 1 + horizon_bars]
        future_lows = low_prices[index + 1 : index + 1 + horizon_bars]

        for future_high, future_low in zip(future_highs, future_lows):
            hit_take_profit = future_high >= upper_barrier
            hit_stop_loss = future_low <= lower_barrier

            if hit_take_profit and hit_stop_loss:
                labels[index] = {
                    "stop_loss": -1,
                    "take_profit": 1,
                    "neutral": 0
                }[same_bar_policy]
                break

            if hit_take_profit:
                labels[index] = 1
                break

            if hit_stop_loss:
                labels[index] = -1
                break

    df["Target"] = labels

    return df