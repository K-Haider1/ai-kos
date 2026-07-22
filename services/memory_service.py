"""
AI-KOS Memory Service
Author: Kahkashan Haider
"""

from memory.conversation_memory import ConversationMemory


class MemoryService:
    """
    Service responsible for managing conversation memory.
    """

    def __init__(self, memory=None):
        self.memory = memory or ConversationMemory()

    def save(
        self,
        query: str,
        answer: str,
    ) -> None:
        """
        Stores a conversation.
        """
        self.memory.add_interaction(
            query=query,
            answer=answer,
        )

    def history(self):
        """
        Returns all conversation history.
        """
        return self.memory.get_history()

    def recent(
        self,
        n: int = 5,
    ):
        """
        Returns the last N interactions.
        """
        return self.memory.get_last(n)

    def clear(self):
        """
        Clears memory.
        """
        self.memory.clear()