"""
Application Settings

Centralized configuration management for AI-KOS.
Sensitive values are loaded from environment variables.

Author: Kahkashan Haider
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application configuration loaded from environment variables."""

    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")
    LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3.5-flash")
    LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.2"))
    LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "1024"))

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

settings = Settings()
