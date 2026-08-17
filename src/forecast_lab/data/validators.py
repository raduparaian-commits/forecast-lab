import pandas as pd

def validate_ohlcv(df: pd.DataFrame) -> bool:
    required_columns = {
        "Timestamp",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    }

    missing_columns = required_columns.difference(df.columns)

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    missing_values = df.isna().sum()

    if missing_values.any():
        raise ValueError(f"Missing values found:/n{missing_values[missing_values > 0]}")

    if not df["Timestamp"].is_monotonic_increasing:
        raise ValueError("Timestamp are not sorted")

    return True