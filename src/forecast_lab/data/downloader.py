import requests
from hashlib import sha256
from pathlib import Path
from time import sleep
from xml.etree import ElementTree


BASE_URL = "https://data.binance.vision/"
MAX_RETRIES = 3


def get_available_files(symbol: str, interval: str) -> list[str]:
    prefix = f"data/spot/monthly/klines/{symbol}/{interval}/"

    response = requests.get(BASE_URL, params={"prefix": prefix}, timeout=30)
    response.raise_for_status()

    root = ElementTree.fromstring(response.text)

    files = []

    for item in root.findall(".//{*}Key"):
        if item.text and item.text.endswith(".zip"):
            files.append(item.text)

    return files


def download_file(url: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, timeout=60)
            response.raise_for_status()

            output_path.write_bytes(response.content)
            return

        except requests.RequestException:
            if attempt == MAX_RETRIES - 1:
                raise

            sleep(2)


def calculate_hash(file_path: Path) -> str:
    hash_function = sha256()

    with file_path.open("rb") as file:
        while chunk := file.read(1024 * 1024):
            hash_function.update(chunk)

    return hash_function.hexdigest()


def verify_checksum(file_path: Path, checksum_path: Path) -> bool:
    expected = checksum_path.read_text().split()[0]
    actual = calculate_hash(file_path)

    return expected == actual


def download_file_with_checksum(file_key: str, output_dir: Path) -> None:
    filename = Path(file_key).name

    zip_path = output_dir / filename
    checksum_path = output_dir / f"{filename}.CHECKSUM"

    if zip_path.exists() and checksum_path.exists() and verify_checksum(zip_path, checksum_path):
        print(f"Verified {filename}")
        return

    zip_url = f"{BASE_URL}{file_key}"
    checksum_url = f"{zip_url}.CHECKSUM"

    for attempt in range(MAX_RETRIES):
        try:
            print(f"Downloading {filename}")

            download_file(zip_url, zip_path)
            download_file(checksum_url, checksum_path)

            if verify_checksum(zip_path, checksum_path):
                print(f"Verified {filename}")
                return

            print(f"Checksum failed {filename}, retrying")

            zip_path.unlink(missing_ok=True)
            checksum_path.unlink(missing_ok=True)

        except Exception:
            if attempt == MAX_RETRIES - 1:
                raise

            sleep(2)

    raise ValueError(f"Failed to download {filename}")


def download_symbol_interval(symbol: str, interval: str, output_dir: Path) -> None:
    files = get_available_files(symbol, interval)

    destination = output_dir / symbol / interval

    for file_key in files:
        download_file_with_checksum(file_key, destination)


def download(symbols: list[str], intervals: list[str], output_dir: Path) -> None:
    for symbol in symbols:
        for interval in intervals:
            download_symbol_interval(symbol, interval, output_dir)