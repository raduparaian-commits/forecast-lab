from pathlib import Path
from typing import Any

import yaml

def load_settings(settings_path: str | Path) -> dict[str, Any]:
    settings_path = Path(settings_path)

    if not settings_path.is_file():
        raise FileNotFoundError(f"Settings file not found: {settings_path}")

    with settings_path.open("r", encoding="utf-8") as settings_file:
        settings = yaml.safe_load(settings_file)

    if not isinstance(settings, dict):
        raise ValueError(f"Settings must contain a mapping: {settings_path}")

    return settings