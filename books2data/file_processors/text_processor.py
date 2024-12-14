from pathlib import Path
import logging
from books2data.utils import detect_encoding

logger = logging.getLogger(__name__)

class TextFileProcessor:
    def __init__(self):
        pass
    
    def process(self, file_path: Path, target_encoding: str, output_dir: Path, subdir_name: str, save_as_text: bool) -> tuple[str, Path]:
        """Processes a text file."""
        try:
            encoding = detect_encoding(file_path) # detect encoding
            with open(file_path, "r", encoding=encoding) as f:
                content = f.read()

            logger.debug(f"Extracted text before saving: {content.strip()}")
            return content.strip(), None
        
        except Exception as e:
            logger.error(f"Error processing Text file: {e}")
            return None, None