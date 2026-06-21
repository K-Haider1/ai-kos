"""
Module: Chunker
Purpose: 
Split cleaned text into meaningful chunks.
Author:
Kahkashan Haider
"""

from typing import List

def chunk_text(
        text: str,
        chunk_size: int = 200,
        chunk_overlap: int = 20 
) -> list[str]:
    """
    Split text into chunks while preserving words.
    Args:
        text: Cleaned text.
        chunk_size: The maximum chunk size.
        chunk_overlap: The number of words to overlapping.
    Returns:
        A list of chunks.
    """
    words = text.split()
    chunks = []
    start = 0
    while start <len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - chunk_overlap
    return chunks

if __name__ == "__main__":
    sample_text = (
        "Artificial Intelligence (AI) is transforming the way we interact with technology. "
        *20
    )

    chunks = chunk_text(sample_text)
    print(f"Total Chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\nChunk {index}")
        print(chunk[:100])  # Print the first 100 characters of each chunk for brevity
