"""
Module: Chunker
Purpose: 
Split cleaned text into chunks for embedding
Author:
Kahkashan Haider
"""

def chunk_text(
        text: str,
        chunk_size: int = 200,
        chunk_overlap: int = 20 
) -> list[str]:
    """
    Split text into overlapping chunks.
    Args:
        text: The cleaned text to be chunked.
        chunk_size: The maximum size of each chunk.
        chunk_overlap: The number of overlapping characters between chunks.
    Returns:
        A list of text chunks.
    """
    chunks = []
    start = 0
    while start <len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
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
