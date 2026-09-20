import argparse
from pathlib import Path

from forecast_lab.data.builder import build
from forecast_lab.data.downloader import download
from forecast_lab.data.extractor import extract_all


def main():
    parser = argparse.ArgumentParser(description="Crypto market data pipeline")

    subparsers = parser.add_subparsers(dest="command", required=True)

    download_parser = subparsers.add_parser("download")
    download_parser.add_argument("symbols", nargs="+")
    download_parser.add_argument("--intervals", nargs="+", required=True)
    download_parser.add_argument("--output-dir", type=Path, required=True)

    extract_parser = subparsers.add_parser("extract")
    extract_parser.add_argument("--input-dir", type=Path, required=True)

    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("--input-dir", type=Path, required=True)
    build_parser.add_argument("--output-dir", type=Path, required=True)

    args = parser.parse_args()

    if args.command == "download":
        download(
            symbols=args.symbols,
            intervals=args.intervals,
            output_dir=args.output_dir,
        )

    elif args.command == "extract":
        extract_all(args.input_dir)

    elif args.command == "build":
        build(
            input_dir=args.input_dir,
            output_dir=args.output_dir,
        )


if __name__ == "__main__":
    main()