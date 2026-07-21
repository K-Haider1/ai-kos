"""
Tests for AI-KOS Report Generator Agent
Author: Kahkashan Haider
"""

import pytest

from agents.report_generator.report_generator_agent import (
    ReportGeneratorAgent,
)


def test_generate_report():

    agent = ReportGeneratorAgent()

    report = agent.generate_report(
        query="What is RAG?",
        answer="RAG combines retrieval with generation.",
    )

    assert report == {
        "query": "What is RAG?",
        "answer": "RAG combines retrieval with generation.",
    }


def test_generate_report_strips_whitespace():

    agent = ReportGeneratorAgent()

    report = agent.generate_report(
        query="  What is RAG?  ",
        answer="  RAG combines retrieval with generation.  ",
    )

    assert report["query"] == "What is RAG?"
    assert report["answer"] == (
        "RAG combines retrieval with generation."
    )


def test_empty_query_raises_error():

    agent = ReportGeneratorAgent()

    with pytest.raises(
        ValueError,
        match="Query cannot be empty.",
    ):
        agent.generate_report(
            query="   ",
            answer="Valid answer",
        )


def test_empty_answer_raises_error():

    agent = ReportGeneratorAgent()

    with pytest.raises(
        ValueError,
        match="Answer cannot be empty.",
    ):
        agent.generate_report(
            query="Valid query",
            answer="   ",
        )