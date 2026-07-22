"""
AI-KOS Conversation Memory
Author: Kahkashan Haider
"""


class ConversationMemory:
    """
    Stores conversation history for the current session.
    """

    def __init__(self):
        self._messages = []

    def add_interaction(
        self,
        query: str,
        answer: str,
    ) -> None:

        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        if not answer or not answer.strip():
            raise ValueError("Answer cannot be empty.")

        self._messages.append(
            {
                "query": query.strip(),
                "answer": answer.strip(),
            }
        )

    def get_history(self):
        """
        Returns all stored interactions.
        """
        return self._messages.copy()

    def get_last(self, n: int = 5):
        """
        Returns the last N interactions.
        """
        if n <= 0:
            raise ValueError("n must be greater than zero.")

        return self._messages[-n:]

    def clear(self):
        """
        Clears conversation history.
        """
        self._messages.clear()