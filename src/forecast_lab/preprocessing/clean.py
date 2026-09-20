import numpy as np
import pandas as pd

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    cleaned_data = data.replace([np.inf, -np.inf], np.nan)
    cleaned_data = cleaned_data.drop_duplicates()
    cleaned_data = cleaned_data.dropna()
    cleaned_data = cleaned_data.sort_values("timestamp")
    cleaned_data = cleaned_data.reset_index(drop=True)

    return cleaned_data
