"""
Module : Text Cleaner
Purpose:
Normalize extracted text before chuinking and embedding.
Author :
Kahkashan Haider
"""

import re

def clean_text(text : str) -> str:
    """
    Clean and normalize text.
    Args:
        text: Raw document text.
    Returns :
        Cleaned and normalized text.
    """
    # Remove Excessive whitespaces
    text = re.sub(r"\s+", " ", text)
    # Remove leading/trailing spaces
    text = text.strip()
    return text

if __name__ == "__main__":
    sample_text = """

    Hello      World        

    AI  -   KOS


    """
    print(clean_text(sample_text))