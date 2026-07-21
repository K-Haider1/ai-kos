"""
End-to-End RAG Service
Author: Kahkashan Haider
"""

from agents.retriever.retriever_agent import RetrieverAgent
from agents.validator.validator_agent import ValidatorAgent
from services.context_builder import ContextBuilder
from prompts.prompt_builder import PromptBuilder
from llm.factory import LLMProviderFactory


class RAGService:
    """
    Orchestrates the complete Retrieval-Augmented Generation (RAG) pipeline.
    """

    def __init__(self):
        self.retriever = RetrieverAgent()
        self.validator = ValidatorAgent()
        self.context_builder = ContextBuilder()
        self.prompt_builder = PromptBuilder()
        self.llm_provider = LLMProviderFactory.create()

    def generate_answer(
        self,
        query: str,
        top_k: int = 3,
    ) -> str:

        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        if top_k <= 0:
            raise ValueError("top_k must be greater than zero.")

        retrieval_results = self.retriever.retrieve(
            query=query,
            top_k=top_k,
        )

        documents = retrieval_results.get("documents", [[]])

        if not documents or not documents[0]:
            return "I could not find relevant information in the knowledge base."

        valid_documents = self.validator.validate_documents(
            documents[0]
        )

        if not valid_documents:
            return "I could not find relevant information in the knowledge base."

        context = self.context_builder.build_context(
            valid_documents
        )

        if not context.strip():
            return "I could not find relevant information in the knowledge base."

        prompt = self.prompt_builder.build_prompt(
            question=query.strip(),
            context=context,
        )

        return self.llm_provider.generate(prompt)