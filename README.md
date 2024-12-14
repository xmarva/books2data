# books2data

Tools for extracting text from various file formats

## WIP

- [ ] Encodings processing
- [ ] .epub
- [ ] .doc, docx
- [ ] .pdf


## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/xmarva/books2data.git
    cd books2data
    ```

2.  Create virtual environment and install dependencies:
    ```bash
     python3 -m venv venv
     source venv/bin/activate
    
     pip install -r requirements.txt
     pip install .
     ```

3. Install `pandoc`

## Notes

### Processing a Directory

To process all .fb2 and .txt files in a directory and save the data to `output.json` in the output directory and save converted text files in `output/converted_text` run:

```bash
books2data input_directory --output_dir output --output_json output.json --save_as_text
```

To process all files with a custom file extension (e.g. .epub) use the --file_ext parameter:

```bash
books2data input_directory --output_dir output --output_json output.json --file_ext epub
```

To specify a target encoding use the --encoding parameter:

```bash
books2data input_directory --output_dir output --output_json output.json --encoding 'windows-1251'
```

To skip saving converted text files, just remove the --save_as_text parameter:

```bash
books2data input_directory --output_dir output --output_json output.json
```

### Processing a Single File
To process a single file (e.g. an .fb2 or .txt file), use the path to the file as the input path:

```bash
books2data input_file.fb2 --output_dir output --output_json output.json --save_as_text
```

or

```bash
books2data input_file.txt --output_dir output --output_json output.json
```

### Debug Mode
To enable debug mode, use --debug parameter:

```bash
books2data input_directory --output_dir output --output_json output.json --debug
```