"""
Module : 
PDF Loader

Purpose: 
This module provides functionality to load and extract text from documents.

Author : 
Kahkashan Haider
"""
from pathlib import Path

def load_text_file(file_path:str) -> str:
    """
    Load text from a text file.
    Args:
        file_path: Path to the file
    Returns:
        The extracted text content
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"The File Not Found : {file_path}")
    return path.read_text(encoding="utf-8")

if __name__ == "__main__":
    text = load_text_file("data/raw/sample_document.txt")
    print(text)