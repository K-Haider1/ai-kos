"""
AI-KOS Multi-Agent Orchestrator Demo
Author: Kahkashan Haider
"""

from services.orchestrator_service import OrchestratorService


def main():

    orchestrator = OrchestratorService()

    query = "What is Retrieval-Augmented Generation?"

    print("\nUSER QUESTION:\n")
    print(query)

    response = orchestrator.execute(query)

    print("\nAI-KOS RESPONSE:\n")
    print(response)


if __name__ == "__main__":
    main()