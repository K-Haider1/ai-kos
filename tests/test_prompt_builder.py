from prompts.prompt_builder import PromptBuilder

def test_prompt_builder():
    builder = PromptBuilder()
    prompt = builder.build_prompt(
        "What is AI ?",
        "Artificial Intelligence Context"
    )
    assert "What is AI ?" in prompt
    assert "Artificial Intelligence Context" in prompt