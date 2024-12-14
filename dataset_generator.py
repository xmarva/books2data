# text_processing_lib/dataset_generator.py
import os
import json
import argparse
from pathlib import Path
from text_processing_lib.core.file_detector import FileDetector
from text_processing_lib.core.text_extractor import TextExtractor
from text_processing_lib.io.file_writer import FileWriter
from text_processing_lib.io.dataset_writer import DatasetWriter
from text_processing_lib.file_handlers.fb2_handler import FB2Handler
from text_processing_lib.file_handlers.txt_handler import TextHandler
from text_processing_lib.file_handlers.document_handler import DocumentHandler


class DatasetGenerator:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.file_detector = FileDetector()
        self.text_extractor = TextExtractor()
        self.file_writer = FileWriter()
        self.dataset_writer = DatasetWriter()
        self.fb2_handler = FB2Handler()
        self.text_handler = TextHandler()
        self.doc_handler = DocumentHandler()

    def process_files(self):
        """Processes book files and saves cleaned text to a combined JSONL and individual TXT files."""
        os.makedirs(self.output_dir, exist_ok=True)
        jsonl_output_path = os.path.join(self.output_dir, "dataset.json")
        all_data = []

        for author_dir_name in os.listdir(self.input_dir):
            if author_dir_name.startswith('.'):
                continue  # Skip hidden files
            author_dir_path = os.path.join(self.input_dir, author_dir_name)
            if os.path.isdir(author_dir_path):
                for filename in os.listdir(author_dir_path):
                    if filename.startswith('.'):
                        continue
                    filepath = os.path.join(author_dir_path, filename)
                    if os.path.isfile(filepath):
                        author = author_dir_name
                        file_type = self.file_detector.detect_file_type(filepath)
                        text = ""
                        if file_type == ".fb2":
                          text = self.fb2_handler.extract_text(filepath)
                        elif file_type == ".txt":
                            text = self.text_handler.extract_text(filepath)
                        elif file_type == ".doc":
                            text = self.doc_handler.extract_text_from_doc(filepath)
                        elif file_type == ".docx":
                            text = self.doc_handler.extract_text_from_docx(filepath)
                        else:
                           print(f"Skipping file {filename} due to unknown file type")
                           continue

                        if text:
                           cleaned_text = self.text_extractor.clean_text(text)
                           all_data.append({"text": cleaned_text, "author": author, "filename": filename})
                           
                           # Save individual author's txt
                           author_output_dir = os.path.join(self.output_dir, author)
                           os.makedirs(author_output_dir, exist_ok=True)
                           author_txt_path = os.path.join(author_output_dir, f"{os.path.splitext(filename)[0]}.txt")
                           self.file_writer.write_text_file(cleaned_text, author_txt_path)
                        else:
                           print(f"Skipping file {filename} because text is empty")


        # Save JSONL
        self.dataset_writer.write_dataset(all_data, jsonl_output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a dataset from text files.")

    parser.add_argument("input_dir", type=str, help="Path to the input directory.")
    parser.add_argument(
        "--output_dir", type=str, default="./processed_data", help="Path to the output directory. Default is ./processed_data"
    )
    args = parser.parse_args()

    input_directory = args.input_dir
    output_directory = args.output_dir

    generator = DatasetGenerator(input_directory, output_directory)
    generator.process_files()