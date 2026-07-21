import pytest

from agents.critic.critic_agent import CriticAgent


def test_review_valid_report():
    agent = CriticAgent()

    report = {
        "query": "What is RAG?",
        "answer": "RAG combines retrieval with generation.",
    }

    result = agent.review(report)

    assert result == {
        "query": "What is RAG?",
        "answer": "RAG combines retrieval with generation.",
        "status": "approved",
    }


def test_review_strips_whitespace():
    agent = CriticAgent()

    report = {
        "query": "  What is RAG?  ",
        "answer": "  RAG combines retrieval and generation.  ",
    }

    result = agent.review(report)

    assert result["query"] == "What is RAG?"
    assert result["answer"] == (
        "RAG combines retrieval and generation."
    )


def test_invalid_report_type_raises_error():
    agent = CriticAgent()

    with pytest.raises(
        ValueError,
        match="Report must be a dictionary.",
    ):
        agent.review("invalid report")


def test_empty_query_raises_error():
    agent = CriticAgent()

    with pytest.raises(
        ValueError,
        match="Report query cannot be empty.",
    ):
        agent.review(
            {
                "query": "   ",
                "answer": "Valid answer",
            }
        )


def test_empty_answer_raises_error():
    agent = CriticAgent()

    with pytest.raises(
        ValueError,
        match="Report answer cannot be empty.",
    ):
        agent.review(
            {
                "query": "Valid query",
                "answer": "   ",
            }
        )