import pandas as pd
from pathlib import Path

def load_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)

    return df

def load_parquet(path: Path) -> pd.DataFrame:
    df = pd.read_parquet(path)

    return df