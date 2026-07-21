"""
Tests for Planner Agent
"""

import pytest

from agents.planner.planner_agent import PlannerAgent


def test_create_knowledge_query_plan():

    agent = PlannerAgent()

    plan = agent.create_plan(
        "What is Retrieval-Augmented Generation?"
    )

    assert plan["query"] == (
        "What is Retrieval-Augmented Generation?"
    )

    assert plan["query_type"] == "knowledge_query"

    assert plan["steps"] == [
        "retrieve_relevant_documents",
        "build_context",
        "generate_grounded_answer",
    ]


def test_create_general_query_plan():

    agent = PlannerAgent()

    plan = agent.create_plan("Hello there")

    assert plan["query_type"] == "general_query"

    assert plan["steps"] == [
        "generate_direct_answer",
    ]


def test_create_plan_strips_whitespace():

    agent = PlannerAgent()

    plan = agent.create_plan(
        "   What is RAG?   "
    )

    assert plan["query"] == "What is RAG?"


def test_empty_query_raises_error():

    agent = PlannerAgent()

    with pytest.raises(
        ValueError,
        match="Query cannot be empty."
    ):
        agent.create_plan("   ")