import pandas as pd

def split_time_series(df: pd.DataFrame, features: list[str], test_size: float | int, horizon_bars: int) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    if "Target" not in df.columns:
        raise KeyError("DataFrame must contain a Target column")

    if "Target" in features:
        raise ValueError("Target cannot be included in features")

    missing_features = set(features).difference(df.columns)

    if missing_features:
        raise KeyError(f"Missing feature columns: {sorted(missing_features)}")

    if not 0 < test_size < 1:
        raise ValueError("test_size must be between zero and one")

    if horizon_bars < 0:
        raise ValueError("horizon_bars cannot be negative")

    if df["Target"].isna().any():
        raise ValueError("Target must not contain missing values")

    if not df["Target"].isin([-1, 0, 1]).all():
        raise ValueError("Target values must be -1, 0, or 1")

    split_index = int(len(df) * (1 - test_size))
    train_end = split_index - horizon_bars

    if train_end <= 0 or split_index >= len(df):
        raise ValueError("DataFrame is too small for the requested split")

    x = df[features]
    y = (df["Target"] + 1).astype(int)
    x_train = x.iloc[:train_end].copy()
    x_test = x.iloc[split_index:].copy()
    y_train = y.iloc[:train_end].copy()
    y_test = y.iloc[split_index:].copy()

    return x_train, x_test, y_train, y_test