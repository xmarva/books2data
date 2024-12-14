import os
import chardet
from pathlib import Path
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

def create_directory(path: Path):
    """Creates a directory if it does not exist."""
    if not path.exists():
        try:
            path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            logger.error(f"Error creating directory '{path}': {e}")

def detect_encoding(file_path: Path) -> str:
    """Detects the encoding of a text file or extracts from FB2 XML header."""
    try:
        with open(file_path, "rb") as f:
            raw_data = f.read(10000)
            
        try:
            tree = ET.fromstring(raw_data)
            if "encoding" in tree.attrib:
                 fb2_encoding = tree.attrib["encoding"]
                 logger.debug(f"Encoding extracted from FB2 header: {fb2_encoding}")
                 return fb2_encoding
        except ET.ParseError:
            pass # File is probably not XML, lets try other methods
            
        result = chardet.detect(raw_data)
        encoding = result["encoding"]
        if encoding is None:
              logger.warning(f"Encoding not detected for {file_path}. Using 'utf-8' as fallback.")
              return "utf-8"
        return encoding
    except Exception as e:
        logger.error(f"Error detecting encoding for '{file_path}': {e}. Using 'utf-8' as default.")
        return "utf-8"