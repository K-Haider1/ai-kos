import pytest

from llm.base import BaseLLMProvider

def test_base_llm_provider_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseLLMProvider()  # Attempt to instantiate the abstract class