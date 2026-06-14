from ingestion.text_cleaner import clean_text

def test_clean_text():
    raw_text = """

    Hello      World        

    AI  -   KOS


    """
    cleaned = clean_text(raw_text)
    assert cleaned =="Hello World AI - KOS"
    # Test that excessive whitespaces are removed
    assert "  " not in cleaned, "Excessive whitespaces not removed"
    
    # Test that leading/trailing spaces are removed
    assert cleaned == "Hello World AI - KOS", "Leading/trailing spaces not removed or text not cleaned properly"
    
    print("All tests passed for clean_text function")