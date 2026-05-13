import os
from pathlib import Path

DATASET = "fever"
ROOT_DIR = Path(__file__).resolve().parent / DATASET
DATA_DIR = ROOT_DIR / "data"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
DB_PATH = PROCESSED_DATA_DIR / "data.db"
