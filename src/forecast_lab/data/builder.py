from pathlib import Path

import pandas as pd


COLUMNS = [
    "timestamp",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "close_timestamp",
    "quote_volume",
    "trades",
    "taker_buy_base_volume",
    "taker_buy_quote_volume",
    "ignore",
]


def build_parquet(input_dir: Path, output_dir: Path) -> None:
    csv_files = sorted(input_dir.glob("*.csv"))

    if not csv_files:
        return

    frames = []

    for csv_file in csv_files:
        print(f"Loading {csv_file.name}")

        df = pd.read_csv(csv_file, header=None, names=COLUMNS)
        frames.append(df)

    dataset = pd.concat(frames, ignore_index=True)

    dataset = dataset.sort_values("timestamp")

    dataset["timestamp"] = pd.to_datetime(dataset["timestamp"], unit="ms")
    dataset["close_timestamp"] = pd.to_datetime(dataset["close_timestamp"], unit="ms")

    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{input_dir.name}.parquet"

    dataset.to_parquet(output_file, index=False)

    print(f"Created {output_file}")

    for csv_file in csv_files:
        csv_file.unlink()

        print(f"Removed {csv_file.name}")


def build(input_dir: Path, output_dir: Path) -> None:
    for symbol_dir in input_dir.iterdir():
        if not symbol_dir.is_dir():
            continue

        for interval_dir in symbol_dir.iterdir():
            if not interval_dir.is_dir():
                continue

            print(f"Building {symbol_dir.name} {interval_dir.name}")

            build_parquet(interval_dir, output_dir / symbol_dir.name)