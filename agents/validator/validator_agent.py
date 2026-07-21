"""
AI-KOS Validator Agent
Author: Kahkashan Haider
"""

from typing import List


class ValidatorAgent:
    """
    Validates retrieved documents before they are used
    for grounded answer generation.
    """

    def validate_documents(
        self,
        documents: List[str],
    ) -> List[str]:

        if not documents:
            return []

        valid_documents = [
            document.strip()
            for document in documents
            if document and document.strip()
        ]

        return valid_documents