from pathlib import Path
from zipfile import ZipFile


def extract_zip(zip_path: Path) -> None:
    output_dir = zip_path.parent

    with ZipFile(zip_path, "r") as archive:
        archive.extractall(output_dir)

    zip_path.unlink()

    checksum_path = Path(f"{zip_path}.CHECKSUM")

    if checksum_path.exists():
        checksum_path.unlink()


def extract_all(input_dir: Path) -> None:
    zip_files = list(input_dir.rglob("*.zip"))

    for zip_path in zip_files:
        print(f"Extracting {zip_path.name}")

        extract_zip(zip_path)

        print(f"Extracted {zip_path.name}")