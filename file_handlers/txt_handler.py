import codecs
from text_processing_lib.core.encoding_handler import EncodingHandler


class TextHandler:
    def __init__(self):
         self.encoding_handler = EncodingHandler()

    def extract_text(self, file_path):
        """Extracts text from a TXT file."""
        text = ""
        try:
            encoding = self.encoding_handler.detect_encoding(file_path) 
            with codecs.open(file_path, "r", encoding=encoding, errors='replace') as f:
              text = f.read() 
            return self.encoding_handler.convert_text(text, input_encoding=encoding, output_encoding='utf-8')
        except Exception as e:
            print(f"Error processing TXT {file_path}: {e}")
        return text.strip()