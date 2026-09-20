from pathlib import Path

import pyarrow as pa
import pyarrow.csv as pyarrow_csv
import pyarrow.parquet as pyarrow_parquet

def convert_csv(csv_filename: str, raw_data_directory: str | Path, parquet_data_directory: str | Path, compression: str = "snappy") -> Path:
    csv_path = Path(raw_data_directory) / csv_filename

    if not csv_path.is_file():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    output_directory = Path(parquet_data_directory)

    if not output_directory.is_dir():
        raise FileNotFoundError(f"Parquet directory not found: {output_directory}")

    parquet_path = output_directory / f"{csv_path.stem}.parquet"

    with pyarrow_csv.open_csv(csv_path) as reader:
        writer = pyarrow_parquet.ParquetWriter(parquet_path, reader.schema, compression=compression)
        try:
            for batch in reader:
                writer.write_table(pa.Table.from_batches([batch]))
        finally:
            writer.close()

    return parquet_path