"""
Tests for AI-KOS History Formatter
Author: Kahkashan Haider
"""

import pytest

from memory.history_formatter import HistoryFormatter


def test_empty_history_returns_empty_string():
    formatter = HistoryFormatter()

    assert formatter.format([]) == ""


def test_none_history_raises_error():
    formatter = HistoryFormatter()

    with pytest.raises(ValueError):
        formatter.format(None)


def test_invalid_history_type_raises_error():
    formatter = HistoryFormatter()

    with pytest.raises(ValueError):
        formatter.format("invalid")


def test_invalid_interaction_type_raises_error():
    formatter = HistoryFormatter()

    history = [
        "invalid"
    ]

    with pytest.raises(ValueError):
        formatter.format(history)


def test_format_single_interaction():
    formatter = HistoryFormatter()

    history = [
        {
            "query": "What is RAG?",
            "answer": "RAG combines retrieval and generation.",
        }
    ]

    formatted = formatter.format(history)

    assert "Conversation History" in formatted
    assert "User:" in formatted
    assert "Assistant:" in formatted
    assert "What is RAG?" in formatted
    assert "RAG combines retrieval and generation." in formatted


def test_format_multiple_interactions():
    formatter = HistoryFormatter()

    history = [
        {
            "query": "Hello",
            "answer": "Hi!"
        },
        {
            "query": "Explain embeddings",
            "answer": "Embeddings convert text into vectors."
        },
    ]

    formatted = formatter.format(history)

    assert formatted.count("User:") == 2
    assert formatted.count("Assistant:") == 2


def test_skip_empty_query():
    formatter = HistoryFormatter()

    history = [
        {
            "query": "",
            "answer": "Answer"
        }
    ]

    assert formatter.format(history) == "Conversation History"


def test_skip_empty_answer():
    formatter = HistoryFormatter()

    history = [
        {
            "query": "Question",
            "answer": ""
        }
    ]

    assert formatter.format(history) == "Conversation History"
    