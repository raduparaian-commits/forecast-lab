from pathlib import Path

import pandas as pd

def save_parquet(data: pd.DataFrame, output_path: str | Path, compression: str = "snappy") -> Path:
    parquet_path = Path(output_path)

    if not parquet_path.parent.is_dir():
        raise FileNotFoundError(f"Directory not found: {parquet_path.parent}")

    data.to_parquet(parquet_path, index=False, compression=compression)

    return parquet_path