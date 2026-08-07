"""
AI-KOS History Formatter
Author: Kahkashan Haider
"""


class HistoryFormatter:
    """
    Formats conversation history into a prompt-ready string.
    """

    def format(self, history: list[dict]) -> str:
        """
        Convert conversation history into a readable format.

        Example:

        Conversation History

        User:
        What is RAG?

        Assistant:
        Retrieval-Augmented Generation...
        """

        if history is None:
            raise ValueError(
                "History cannot be None."
            )

        if not isinstance(history, list):
            raise ValueError(
                "History must be a list."
            )

        if len(history) == 0:
            return ""

        sections = ["Conversation History\n"]

        for interaction in history:

            if not isinstance(interaction, dict):
                raise ValueError(
                    "Each interaction must be a dictionary."
                )

            query = interaction.get("query", "").strip()
            answer = interaction.get("answer", "").strip()

            if not query:
                continue

            if not answer:
                continue

            sections.append(
                f"User:\n{query}\n\n"
                f"Assistant:\n{answer}\n"
            )

        return "\n".join(sections).strip()