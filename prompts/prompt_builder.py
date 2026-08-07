"""
AI-KOS Prompt Builder
Author: Kahkashan Haider
"""


class PromptBuilder:
    """
    Builds the final prompt that is sent to the LLM.

    The prompt can include:

    - Conversation history
    - Retrieved knowledge
    - Current user question
    """

    def build_prompt(
        self,
        query: str,
        context: str,
        history: str = "",
    ) -> str:
        """
        Build the final prompt.

        Parameters
        ----------
        query : str
            Current user question.

        context : str
            Retrieved RAG context.

        history : str
            Previous conversation history.
        """

        if not isinstance(query, str):
            raise ValueError("Query must be a string.")

        if not isinstance(context, str):
            raise ValueError("Context must be a string.")

        if not isinstance(history, str):
            raise ValueError("History must be a string.")

        query = query.strip()
        context = context.strip()
        history = history.strip()

        if not query:
            raise ValueError("Query cannot be empty.")

        prompt_parts = []

        if history:
            prompt_parts.append(history)

        if context:
            prompt_parts.append(
                f"Retrieved Context\n\n{context}"
            )

        prompt_parts.append(
            f"Current User Question\n\n{query}"
        )

        prompt_parts.append(
            (
                "Answer the user's question using the "
                "retrieved context when available. "
                "If previous conversation is relevant, "
                "use it to provide a coherent response."
            )
        )

        return "\n\n----------------------------------------\n\n".join(
            prompt_parts
        )
