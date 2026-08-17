from pathlib import Path

import pandas as pd

from forecast_lab.data import validate_ohlcv


CSV_PATH = Path("../data/raw/btc_usd_1min.csv")


df = pd.read_csv(CSV_PATH)

is_valid = validate_ohlcv(df)

print("Valid:", is_valid)