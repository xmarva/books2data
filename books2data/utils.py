import os
import chardet
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def create_directory(path: Path):
    """Creates a directory if it does not exist."""
    if not path.exists():
        try:
            path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            logger.error(f"Error creating directory '{path}': {e}")

def detect_encoding(file_path: Path) -> str:
    """Detects the encoding of a text file."""
    try:
        with open(file_path, "rb") as f:
             raw_data = f.read(10000)
             result = chardet.detect(raw_data)
             encoding = result["encoding"]
        if encoding is None:
            return "utf-8"
        return encoding
    except Exception as e:
         logger.error(f"Error detecting encoding for '{file_path}': {e}. Using 'utf-8' as default.")
         return "utf-8"