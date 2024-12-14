# text_processing_lib/core/text_extractor.py
import re

class TextExtractor:

    def clean_text(self, text):

        text = re.sub(r'\s*\d+\s*', '', text)
        
        text = re.sub(r'^[A-ZА-ЯЁ]+\s*$', '', text, flags=re.MULTILINE)  # Remove TOC style headings
        text = re.sub(r'^\s*Contents\s*$', '', text, flags=re.MULTILINE | re.IGNORECASE)  # Remove "Contents" word
        text = re.sub(r'^\s*[\.\,\;\:\- ]*\s*$', '', text, flags=re.MULTILINE)  # Remove blank or punctuation-only lines

        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()