# medusa

This is repo with my tools for extracting text from various file formats, handling encodings, and creating structured datasets.

## Supported Formats

*   `.txt` (plain text files)
*   `.fb2` (using `pandoc` for text extraction)
*   `.doc` and `.docx` (using the `textract` library)

## How to Use

1.  Ensure you have the required libraries installed:
    ```bash
    pip install textract chardet beautifulsoup4 python-docx
    ```
   You also need to have `pandoc` installed as system tool.

2.  Run the script from the command line:
    ```bash
    python text_processing_lib/dataset_generator.py /path/to/your/input --output_dir /path/to/your/output
    ```