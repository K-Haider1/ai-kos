from config.settings import settings

def test_default_llm_settings():
    assert settings.LLM_PROVIDER
    assert settings.LLM_MODEL
    assert isinstance(settings.LLM_TEMPERATURE, float)
    assert isinstance(settings.LLM_MAX_TOKENS, int)