import argparse
import logging
from books2data.core import BookProcessor
from pathlib import Path

def setup_logging(level: int = logging.INFO):
    """Sets up logging configuration."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def main():
    parser = argparse.ArgumentParser(description="Process book files and extract data.")
    parser.add_argument(
        "input_path",
        help="Path to the input directory or file.",
    )
    parser.add_argument(
        "--output_dir",
        default="output",
        help="Directory to save converted text files and JSON output.",
    )
    parser.add_argument(
        "--output_json",
        default="output.json",
        help="Path to the output JSON file.",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Target encoding for the text files.",
    )
    parser.add_argument(
        "--save_as_text",
        action="store_true",
        help="Saves converted text files in txt format to a 'converted_text' subdirectory.",
    )
    parser.add_argument(
       "--file_ext",
       default="*",
       help="File extensions to search for when processing a directory",
    )
    parser.add_argument(
       "--debug",
        action="store_true",
        help="Set logging level to debug."
    )

    args = parser.parse_args()
    
    if args.debug:
         setup_logging(logging.DEBUG)
    else:
         setup_logging()

    processor = BookProcessor(args.output_dir, args.encoding, args.save_as_text)
    input_path = Path(args.input_path)
    
    if input_path.is_dir():
        all_data = processor.process_directory(str(input_path), args.file_ext)
        if all_data:
            processor.save_to_json(all_data, args.output_json)
    elif input_path.is_file():
        data = processor.process_file(str(input_path))
        if data:
            processor.save_to_json([data], args.output_json)
    else:
        logging.error(f"Input path not valid: {input_path}")

    processed_files = processor.get_processed_files()
    if processed_files:
        logging.info(f"Processed files: {', '.join(processed_files)}")
    else:
         logging.info("No files were processed.")

if __name__ == "__main__":
    main()