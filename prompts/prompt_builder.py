"""
Prompt Builder
Author : Kahkashan Haider
"""

class PromptBuilder:
    def build_prompt(
            self,
            question : str,
            context : str,
    ) -> str:
        prompt = f"""
You are an AI assistant.
Answer the question only using the provided context.

context:
{context}

question:
{question}

answer:
"""
        return prompt