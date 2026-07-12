from unittest.mock import MagicMock, patch
from llm.providers.gemini_provider import GeminiProvider

@patch(
     "llm.providers.gemini_provider.genai.Client"
)
def test_gemini_generate(mock_client):
    mock_response = MagicMock()
    mock_response.text = "Test AI Generated response"
    mock_instance = mock_client.return_value
    mock_instance.models.generate_content.return_value = (mock_response)

    with patch(
         "llm.providers.gemini_provider.settings.GEMINI_API_KEY",
        "fake-api-key"
    ):
        provider = GeminiProvider()
        response = provider.generate("What is AI ?")
    
    assert response == "Test AI Generated response"
    mock_instance.models.generate_content.assert_called_once()