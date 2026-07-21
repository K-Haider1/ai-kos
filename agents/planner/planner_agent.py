"""
Planner Agent
Author: Kahkashan Haider
"""

from typing import Dict, List


class PlannerAgent:
    """
    Analyzes a user query and creates an execution plan.
    """

    KNOWLEDGE_KEYWORDS = (
        "what",
        "why",
        "how",
        "explain",
        "define",
        "describe",
        "tell me about",
    )

    def create_plan(
        self,
        query: str,
    ) -> Dict[str, str | List[str]]:

        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        cleaned_query = query.strip()
        query_type = self._classify_query(cleaned_query)

        if query_type == "knowledge_query":
            steps = [
                "retrieve_relevant_documents",
                "build_context",
                "generate_grounded_answer",
            ]
        else:
            steps = [
                "generate_direct_answer",
            ]

        return {
            "query": cleaned_query,
            "query_type": query_type,
            "steps": steps,
        }

    def _classify_query(self, query: str) -> str:

        normalized_query = query.lower()

        if normalized_query.startswith(
            self.KNOWLEDGE_KEYWORDS
        ):
            return "knowledge_query"

        return "general_query"