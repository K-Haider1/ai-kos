"""
Gemini LLM Provider
Author: Kahkashan Haider
"""

from google import genai
from google.genai import types

from config.settings import settings
from llm.base import BaseLLMProvider

class GeminiProvider(BaseLLMProvider):

    def __init__(self):
        if not settings.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )
        self.client = genai.Client(
            api_key = settings.GEMINI_API_KEY
        )
    
    def generate(self, prompt: str) -> str:
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")
        
        response = self.client.models.generate_content(
            model = settings.LLM_MODEL,
            contents = prompt,
            config = types.GenerateContentConfig(
                temperature = settings.LLM_TEMPERATURE,
                max_output_tokens = settings.LLM_MAX_TOKENS
            ),
        )
        return response.text or ""
