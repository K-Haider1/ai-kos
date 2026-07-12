"""
LLM Connection Test
Author: Kahkashan Haider
"""

from llm.factory import LLMProviderFactory

def main():
    provider = LLMProviderFactory.create()
    response = provider.generate(
        "Explain Retrieval-Augmented Generation in one sentence."
    )
    print("\nLLM Response:\n")
    print(response)

if __name__ == "__main__":
    main()

