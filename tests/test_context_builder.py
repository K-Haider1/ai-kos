from services.context_builder import ContextBuilder

def test_context_builder():
    builder = ContextBuilder()
    context = builder.build_context(
        [
            "Document One",
            "Document Two"
        ]
    )
    assert "Document One" in context
    assert "Document Two" in context
    