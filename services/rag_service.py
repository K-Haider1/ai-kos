"""
End-to-End RAG Service
Author: Kahkashan Haider
"""

from agents.retriever.retriever_agent import RetrieverAgent
from agents.validator.validator_agent import ValidatorAgent
from services.context_builder import ContextBuilder
from prompts.prompt_builder import PromptBuilder
from llm.factory import LLMProviderFactory
from memory.history_formatter import HistoryFormatter
from services.memory_service import MemoryService

class RAGService:
    """
    Orchestrates the complete Retrieval-Augmented Generation (RAG) pipeline.
    """

    def __init__(
        self,
        retriever=None,
        validator=None,
        context_builder=None,
        prompt_builder=None,
        llm_provider=None,
        memory_service=None,
        history_formatter=None,
    ):
        self.retriever = retriever or RetrieverAgent()

        self.validator = validator or ValidatorAgent()

        self.context_builder = (
            context_builder
            or ContextBuilder()
        )

        self.prompt_builder = (
            prompt_builder
            or PromptBuilder()
        )

        self.llm_provider = (
            llm_provider
            or LLMProviderFactory.create()
        )

        self.memory_service = (
            memory_service
            or MemoryService()
        )

        self.history_formatter = (
            history_formatter
            or HistoryFormatter()
        )
    
    def generate_answer(
        self,
        query: str,
        top_k: int = 3,
        conversation_history=None,
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
            return (
                "I could not find relevant information "
                "in the knowledge base."
            )

        conversation_history = (
            conversation_history or []
        )

        formatted_history = (
            self.history_formatter.format(
                conversation_history
            )
        )

        prompt = self.prompt_builder.build_prompt(
            query=query.strip(),
            context=context,
            history=formatted_history,
        )

        return self.llm_provider.generate(prompt)