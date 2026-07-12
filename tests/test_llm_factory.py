import pytest
from llm.factory import LLMProviderFactory

def test_unsupported_provider():
    with pytest.raises(
        ValueError,
        match="Unsupported LLM provider"
        ):
        LLMProviderFactory.create("unsupported")