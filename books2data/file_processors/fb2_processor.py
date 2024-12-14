from pathlib import Path
import subprocess
import logging
from books2data.utils import create_directory

logger = logging.getLogger(__name__)

class FB2FileProcessor:
    def __init__(self):
        pass

    def process(self, file_path: Path, target_encoding: str, output_dir: Path, subdir_name: str, save_as_text: bool) -> tuple[str, Path]:
        """Processes an FB2 file using pandoc."""
        try:
            text_output_path = output_dir / "converted_text" / subdir_name / file_path.stem
            create_directory(text_output_path.parent)

            if save_as_text:
                command = ["pandoc", str(file_path), "-o", str(text_output_path.with_suffix(".txt"))]
                subprocess.run(command, check=True, capture_output=True) #output to file
            
            command = ["pandoc", str(file_path), "-t", "plain"]
            result = subprocess.run(command, check=True, capture_output=True, text=True) #output to variable
            
            return result.stdout.strip(), text_output_path if save_as_text else None
        except subprocess.CalledProcessError as e:
            logger.error(f"Pandoc error: {e}")
            return None, None
        except Exception as e:
            logger.error(f"Error processing FB2 file: {e}")
            return None, None