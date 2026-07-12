"""
Base LLM Provider Interface
Defines the common contract that every LLM provider in AI-KOS must implement.

Author : Kahkashan Haider
"""

from abc import ABC, abstractmethod

class BaseLLMProvider(ABC):
    """
    Abstract base class for LLM providers.
    """ 

    @abstractmethod
    def generate(self, prompt: str) -> str:

        """
        Generate a response for the supplied prompt.
        
        Args: 
            prompt : Fully constructed prompt sent to the LLM.
        Returns: 
            Generated text response.
        """
        raise NotImplementedError