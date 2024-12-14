# text_processing_lib/core/encoding_handler.py
import codecs
import chardet

class EncodingHandler:

    def detect_encoding(self, file_path):
        try:
            with open(file_path, "rb") as f:
              raw_data = f.read()
              result = chardet.detect(raw_data)
              return result['encoding']
        except Exception as e:
            print(f"Error detecting encoding for {file_path}: {e}")
            return "utf-8" 


    def convert_text(self, text, input_encoding='utf-8', output_encoding='utf-8'):
        try:
            encoded_text = text.encode(input_encoding, errors='ignore') 
            return encoded_text.decode(output_encoding, errors='ignore')
        except UnicodeError as e:
            print(f"Encoding error: {e}")
            return text 
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return text