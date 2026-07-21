"""
Tests for AI-KOS Validator Agent
Author: Kahkashan Haider
"""

from agents.validator.validator_agent import ValidatorAgent


def test_validate_documents():

    agent = ValidatorAgent()

    documents = [
        "Relevant document",
        "",
        "   ",
        None,
        "Another relevant document",
    ]

    result = agent.validate_documents(documents)

    assert result == [
        "Relevant document",
        "Another relevant document",
    ]


def test_empty_documents_returns_empty_list():

    agent = ValidatorAgent()

    result = agent.validate_documents([])

    assert result == []


def test_documents_are_stripped():

    agent = ValidatorAgent()

    documents = [
        "  First document  ",
        " Second document ",
    ]

    result = agent.validate_documents(documents)

    assert result == [
        "First document",
        "Second document",
    ]