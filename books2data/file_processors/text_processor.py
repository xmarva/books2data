from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class TextFileProcessor:
    def __init__(self):
        pass
    
    def process(self, file_path: Path, target_encoding: str, output_dir: Path, subdir_name: str, save_as_text: bool) -> tuple[str, Path]:
        """Processes a text file."""
        try:
            with open(file_path, "r", encoding=target_encoding) as f:
                content = f.read()

            return content.strip(), None
        
        except Exception as e:
           logger.error(f"Error processing Text file: {e}")
           return None, None