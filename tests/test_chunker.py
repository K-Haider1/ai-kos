from ingestion.chunker import chunk_text

def test_chunk_text():

    text = "AI KOS" *100
    chunks = chunk_text(text, 
                        chunk_size=20, 
                        chunk_overlap= 5
                        )
    assert len(chunks) > 1
    assert isinstance(chunks, list)
    