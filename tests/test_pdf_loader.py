from ingestion.pdf_loader import load_text_file

def test_load_text_file():

    text = load_text_file("data/raw/sample_document.txt")
    assert len(text) > 0

    # Test with a valid file path
    try:
        text = load_text_file("data/raw/sample_document.txt")
        assert isinstance(text, str)
        print("Test passed: Valid file path")
    except Exception as e:
        print(f"Test failed: Valid file path - {e}")

    # Test with an invalid file path
    try:
        load_text_file("data/raw/non_existent_file.txt")
        print("Test failed: Invalid file path - No exception raised")
    except FileNotFoundError:
        print("Test passed: Invalid file path - FileNotFoundError raised")
    except Exception as e:
        print(f"Test failed: Invalid file path - Unexpected exception raised - {e}")

