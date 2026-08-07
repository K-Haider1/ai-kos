"""
Tests for RAG Service
Author: Kahkashan Haider
"""

from unittest.mock import MagicMock
from services.rag_service import RAGService


def test_generate_answer():

    rag_service = RAGService()

    # Mock conversation history
    rag_service.memory_service.recent = MagicMock(
        return_value=[]
    )

    # Mock formatted history
    rag_service.history_formatter.format = MagicMock(
        return_value=""
    )

    # Mock retrieval result
    rag_service.retriever.retrieve = MagicMock(
        return_value={
            "documents": [
                [
                    "Retrieval-Augmented Generation combines "
                    "information retrieval with language generation."
                ]
            ]
        }
    )

    # Mock LLM response
    rag_service.llm_provider.generate = MagicMock(
        return_value=(
            "RAG combines information retrieval "
            "with language generation."
        )
    )

    answer = rag_service.generate_answer(
        query="What is RAG?",
        top_k=3,
    )

    assert answer == (
        "RAG combines information retrieval "
        "with language generation."
    )


def test_empty_query_raises_error():

    rag_service = RAGService()

    try:
        rag_service.generate_answer("")
        assert False, "Expected ValueError"

    except ValueError as error:
        assert str(error) == "Query cannot be empty."

def test_empty_retrieval_returns_fallback_message():

    rag_service = RAGService()

    rag_service.memory_service.recent = MagicMock(
        return_value=[]
    )

    rag_service.history_formatter.format = MagicMock(
        return_value=""
    )

    rag_service.retriever.retrieve = MagicMock(
        return_value={
            "documents": [[]]
        }
    )

    rag_service.llm_provider.generate = MagicMock()

    answer = rag_service.generate_answer(
        query="What is an unknown topic?"
    )

    assert answer == (
        "I could not find relevant information "
        "in the knowledge base."
    )

    rag_service.llm_provider.generate.assert_not_called()


def test_blank_documents_return_fallback_message():

    rag_service = RAGService()

    rag_service.memory_service.recent = MagicMock(
        return_value=[]
    )

    rag_service.history_formatter.format = MagicMock(
        return_value=""
    )

    rag_service.retriever.retrieve = MagicMock(
        return_value={
            "documents": [["", "   ", None]]
        }
    )

    rag_service.llm_provider.generate = MagicMock()

    answer = rag_service.generate_answer(
        query="What is an unknown topic?"
    )

    assert answer == (
        "I could not find relevant information "
        "in the knowledge base."
    )

    rag_service.llm_provider.generate.assert_not_called()


def test_invalid_top_k_raises_error():

    rag_service = RAGService()

    try:
        rag_service.generate_answer(
            query="What is RAG?",
            top_k=0,
        )
        assert False, "Expected ValueError"

    except ValueError as error:
        assert str(error) == (
            "top_k must be greater than zero."
        )