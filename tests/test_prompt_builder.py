"""
Tests for Prompt Builder
Author: Kahkashan Haider
"""

import pytest

from prompts.prompt_builder import PromptBuilder


def test_build_prompt_without_history():
    builder = PromptBuilder()

    prompt = builder.build_prompt(
        query="What is RAG?",
        context="RAG combines retrieval and generation.",
    )

    assert "Current User Question" in prompt
    assert "Retrieved Context" in prompt
    assert "Conversation History" not in prompt


def test_build_prompt_with_history():
    builder = PromptBuilder()

    history = (
        "Conversation History\n\n"
        "User: Hello\n"
        "Assistant: Hi!"
    )

    prompt = builder.build_prompt(
        query="Explain embeddings",
        context="Embeddings are vectors.",
        history=history,
    )

    assert "Conversation History" in prompt
    assert "Retrieved Context" in prompt
    assert "Current User Question" in prompt


def test_empty_query_raises_error():
    builder = PromptBuilder()

    with pytest.raises(ValueError):
        builder.build_prompt(
            query="",
            context="context",
        )


def test_invalid_history_type():
    builder = PromptBuilder()

    with pytest.raises(ValueError):
        builder.build_prompt(
            query="Hello",
            context="Context",
            history=[],
        )
        