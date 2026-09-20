from pathlib import Path

import pandas as pd

def load_parquet(parquet_filename: str, parquet_data_directory: str | Path) -> pd.DataFrame:
    parquet_path = Path(parquet_data_directory) / parquet_filename

    if not parquet_path.is_file():
        raise FileNotFoundError(f"Parquet not found: {parquet_path}")

    data = pd.read_parquet(parquet_path)

    return data