import os
import json
from pathlib import Path
from tqdm import tqdm
from typing import Callable, List, Dict, Any, Optional
import logging
from books2data.file_processors.text_processor import TextFileProcessor
from books2data.utils import create_directory, detect_encoding

logger = logging.getLogger(__name__)

class BookProcessor:
    def __init__(self, output_dir: str, target_encoding: str = "utf-8", save_as_text: bool = False):
        self.output_dir = Path(output_dir)
        self.target_encoding = target_encoding
        self.save_as_text = save_as_text
        self.text_processor = TextFileProcessor()
        self.processed_files = []
    
    def _process_file(self, file_path: Path, file_processor: Callable, subdir_name: str) -> Optional[Dict[str, Any]]:
        """Processes a single file using the provided processor."""
        try:
            logger.info(f"Processing: {file_path}")
            encoding = detect_encoding(file_path)
            if encoding != self.target_encoding:
                logger.info(f"Detected encoding: {encoding}, converting to {self.target_encoding}")
            
            data, new_file_path = file_processor(file_path, self.target_encoding, self.output_dir, subdir_name, self.save_as_text)

            if data:
                return {
                        "file_path": str(file_path.relative_to(file_path.parent.parent)),
                        "subdir": subdir_name,
                        "content": data,
                       }
            else:
                return None
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return None

    def process_directory(self, input_dir: str, file_ext: str = "*") -> List[Dict[str, Any]]:
        """Processes all files within a directory (including subdirectories)."""
        input_path = Path(input_dir)
        if not input_path.exists():
            logger.error(f"Input directory does not exist: {input_dir}")
            return []

        all_files = list(input_path.rglob(f"*.{file_ext}"))

        if not all_files:
             logger.warning(f"No files with '{file_ext}' extension found in directory: {input_dir}")
             return []


        if self.save_as_text:
            text_output_dir = self.output_dir / "converted_text"
            create_directory(text_output_dir)


        all_data = []

        for file_path in tqdm(all_files, desc="Processing Files", unit="file", colour="green"):
            subdir_name = str(file_path.relative_to(input_path).parent)
            processed_data = None

            if file_path.suffix == ".fb2":
                from book2data.file_processors.fb2_processor import FB2FileProcessor
                fb2_processor = FB2FileProcessor()
                processed_data = self._process_file(file_path, fb2_processor.process, subdir_name)
            elif file_path.suffix == ".txt":
                processed_data = self._process_file(file_path, self.text_processor.process, subdir_name)
            else:
                logger.warning(f"Skipping file with unsupported extension: {file_path}")
                
            if processed_data:
               all_data.append(processed_data)
               self.processed_files.append(str(file_path))

        return all_data

    def process_file(self, file_path: str) -> Optional[Dict[str, Any]]:
         """Processes a single file."""
         file_path = Path(file_path)

         if not file_path.exists():
             logger.error(f"Input file does not exist: {file_path}")
             return None
         
         if self.save_as_text:
              text_output_dir = self.output_dir / "converted_text"
              create_directory(text_output_dir)
         
         processed_data = None

         subdir_name = "" # single file don't have subdirectories

         if file_path.suffix == ".fb2":
             from book2data.file_processors.fb2_processor import FB2FileProcessor
             fb2_processor = FB2FileProcessor()
             processed_data = self._process_file(file_path, fb2_processor.process, subdir_name)
         elif file_path.suffix == ".txt":
              processed_data = self._process_file(file_path, self.text_processor.process, subdir_name)
         else:
             logger.warning(f"Unsupported file format: {file_path}")
             return None
         
         if processed_data:
             self.processed_files.append(str(file_path))
         
         return processed_data
         
    
    def save_to_json(self, all_data: List[Dict[str, Any]], json_output_path: str):
        """Saves processed data to a JSON file."""
        json_output_path = Path(json_output_path)
        
        try:
            with open(json_output_path, "w", encoding="utf-8") as f:
               json.dump(all_data, f, indent=4, ensure_ascii=False)
            logger.info(f"Data saved to: {json_output_path}")
        except Exception as e:
            logger.error(f"Error saving to json: {e}")
            
    def get_processed_files(self) -> List[str]:
            return self.processed_files