"""
Tests for AI-KOS Orchestrator Service
"""

from services.orchestrator_service import OrchestratorService


class FakePlanner:

    def __init__(self, query_type):
        self.query_type = query_type

    def create_plan(self, query):
        return {
            "query": query.strip(),
            "query_type": self.query_type,
            "steps": [],
        }


class FakeRAGService:

    def generate_answer(self, query):
        return f"RAG answer: {query}"


class FakeLLMProvider:

    def generate(self, prompt):
        return f"Direct answer: {prompt}"


def test_knowledge_query_routes_to_rag():

    orchestrator = OrchestratorService(
        planner=FakePlanner("knowledge_query"),
        rag_service=FakeRAGService(),
        llm_provider=FakeLLMProvider(),
    )

    response = orchestrator.execute(
        "What is RAG?"
    )

    assert response == {
    "query": "What is RAG?",
    "answer": "RAG answer: What is RAG?",
    "status": "approved",
}


def test_general_query_routes_to_llm():

    orchestrator = OrchestratorService(
        planner=FakePlanner("general_query"),
        rag_service=FakeRAGService(),
        llm_provider=FakeLLMProvider(),
    )

    response = orchestrator.execute(
        "Hello there"
    )

    assert response == {
    "query": "Hello there",
    "answer": "Direct answer: Hello there",
    "status": "approved",
}


def test_unsupported_query_type_raises_error():

    orchestrator = OrchestratorService(
        planner=FakePlanner("unsupported"),
        rag_service=FakeRAGService(),
        llm_provider=FakeLLMProvider(),
    )

    try:
        orchestrator.execute("Test query")
        assert False, "Expected ValueError"

    except ValueError as error:
        assert (
            str(error)
            == "Unsupported query type: unsupported"
        )