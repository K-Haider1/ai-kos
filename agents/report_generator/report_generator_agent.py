"""
AI-KOS Report Generator Agent
Author: Kahkashan Haider
"""


class ReportGeneratorAgent:
    """
    Formats a generated answer into the final report structure.
    """

    def generate_report(
        self,
        query: str,
        answer: str,
    ) -> dict:

        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        if not answer or not answer.strip():
            raise ValueError("Answer cannot be empty.")

        return {
            "query": query.strip(),
            "answer": answer.strip(),
        }