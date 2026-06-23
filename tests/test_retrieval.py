from agents.retriever.retriever_agent import RetrieverAgent


def test_retriever_creation():
    agent = RetrieverAgent()
    assert agent is not None