# text_processing_lib/core/file_detector.py
import os

class FileDetector:

    def detect_file_type(self, file_path):
        _, ext = os.path.splitext(file_path)
        return ext.lower()