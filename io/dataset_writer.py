import json
import codecs


class DatasetWriter:

    def write_dataset(self, data, output_path, encoding='utf-8'):
        """Writes data to a JSON file using a given encoding."""
        try:
             with codecs.open(output_path, "w", encoding=encoding) as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
             print(f"Combined data saved in {output_path}")
        except Exception as e:
            print(f"Error while saving json file {output_path}: {e}")