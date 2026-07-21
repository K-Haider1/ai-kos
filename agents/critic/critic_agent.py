"""
AI-KOS Critic Agent
Author: Kahkashan Haider
"""


class CriticAgent:
    """
    Reviews a generated report before it is returned
    as the final AI-KOS response.
    """

    def review(self, report: dict) -> dict:
        if not isinstance(report, dict):
            raise ValueError("Report must be a dictionary.")

        query = report.get("query", "")
        answer = report.get("answer", "")

        if not query or not query.strip():
            raise ValueError("Report query cannot be empty.")

        if not answer or not answer.strip():
            raise ValueError("Report answer cannot be empty.")

        return {
            "query": query.strip(),
            "answer": answer.strip(),
            "status": "approved",
        }