from ingestion.chunker import chunk_text

def test_chunk_text():

    text = "AI KOS" *100
    chunks = chunk_text(text, 
                        chunk_size=100, 
                        chunk_overlap= 10
                        )
    assert len(chunks) > 1
    