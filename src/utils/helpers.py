import yaml
import os
from pathlib import Path


def load_config(path: str = "config.yaml") -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def ensure_directories():
    dirs = ["data/raw_pdfs", "data/vectorstore"]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
