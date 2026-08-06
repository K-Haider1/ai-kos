"""
AI-KOS Orchestrator Service
Author: Kahkashan Haider
"""

from services.memory_service import MemoryService
from agents.critic.critic_agent import CriticAgent
from agents.planner.planner_agent import PlannerAgent
from agents.report_generator.report_generator_agent import (
    ReportGeneratorAgent,
)
from llm.factory import LLMProviderFactory
from services.rag_service import RAGService


class OrchestratorService:
    """
    Routes user queries according to the execution plan
    created by the Planner Agent.

    The generated answer is converted into a structured
    report and reviewed by the Critic Agent before being
    returned as the final response.
    """

    def __init__(
        self,
        planner=None,
        rag_service=None,
        llm_provider=None,
        critic=None,
        report_generator=None,
        memory_service=None,
    ):
        self.planner = planner or PlannerAgent()

        self.rag_service = (
            rag_service
            or RAGService()
        )

        self.llm_provider = (
            llm_provider
            or LLMProviderFactory.create()
        )

        self.report_generator = (
            report_generator
            or ReportGeneratorAgent()
        )

        self.critic = (
            critic
            or CriticAgent()
        )

        self.memory_service = (
            memory_service
            or MemoryService()
        )

    def execute(
        self,
        query: str,
    ) -> dict:

        plan = self.planner.create_plan(query)

        query_type = plan["query_type"]
        cleaned_query = plan["query"]

        # Load recent conversation history
        # (used in upcoming phases)
        conversation_history = (
            self.memory_service.recent()
        )

        if query_type == "knowledge_query":

            answer = self.rag_service.generate_answer(
                cleaned_query
            )

        elif query_type == "general_query":

            answer = self.llm_provider.generate(
                cleaned_query
            )

        else:
            raise ValueError(
                f"Unsupported query type: {query_type}"
            )

        report = self.report_generator.generate_report(
            query=cleaned_query,
            answer=answer,
        )

        reviewed_report = self.critic.review(
            report
        )

        self.memory_service.save(
            query=reviewed_report["query"],
            answer=reviewed_report["answer"],
        )

        return reviewed_report