"""
LLM Provider Factory
Author: Kahkashan Haider
"""

from config.settings import settings
from llm.base import BaseLLMProvider

class LLMProviderFactory:

    @staticmethod
    def create(
        provider_name : str | None = None
    ) -> BaseLLMProvider:
        
        provider = (
            provider_name or settings.LLM_PROVIDER
        ).lower().strip()

        if provider == "gemini":
            from llm.providers.gemini_provider import GeminiProvider
            return GeminiProvider()
        
        raise ValueError(f"Unsupported LLM provider: {provider}")
    