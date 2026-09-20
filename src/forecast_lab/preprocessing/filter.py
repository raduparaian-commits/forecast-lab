import pandas as pd

def filter_by_timestamp(data: pd.DataFrame, start_timestamp: int, timestamp_column: str = "timestamp") -> pd.DataFrame:
    filtered_data = data.loc[data[timestamp_column] >= start_timestamp].copy()

    return filtered_data