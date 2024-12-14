import subprocess
from text_processing_lib.core.encoding_handler import EncodingHandler

class FB2Handler:
    def __init__(self):
         self.encoding_handler = EncodingHandler()
    
    def extract_text(self, file_path):
        """Extracts text from an FB2 file using pandoc."""
        try:
          command = ["pandoc", file_path, "-t", "plain", "-o", "-", "--output-encoding=utf-8"] 
          result = subprocess.run(command, capture_output=True, text=False, check=False)
          if result.returncode != 0:
              print(f"Error processing FB2 {file_path}: pandoc returned non-zero exit status {result.returncode}")
              return ""
          encoding = self.encoding_handler.detect_encoding(file_path)
          text = result.stdout.decode('utf-8', errors='replace').strip() 
          return self.encoding_handler.convert_text(text, input_encoding='utf-8', output_encoding='utf-8')
        except Exception as e:
            print(f"Error processing FB2 {file_path}: {e}")
            return ""