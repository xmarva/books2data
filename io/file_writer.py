import codecs
import os


class FileWriter:

    def write_text_file(self, text, output_path, encoding='utf-8'):
        """Writes text to a file with the specified encoding."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        try:
            with codecs.open(output_path, "w", encoding=encoding) as f:
                f.write(text)
            print(f"File saved in {output_path}")
        except Exception as e:
           print(f"Error while saving file {output_path}: {e}")