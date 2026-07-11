"""
Context Builder Service
Author : Kahkashan Haider
"""
from typing import List

class ContextBuilder:
    def build_context(self, documents: List[str]) -> str:
        if not documents:
            return ""
        context = "\n\n".join(documents)
        return context