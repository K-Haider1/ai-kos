"""
AI-KOS Conversation Memory Demo
Author: Kahkashan Haider
"""

from services.orchestrator_service import OrchestratorService


def main():
    orchestrator = OrchestratorService()

    questions = [
        "What is Retrieval-Augmented Generation?",
        "Can you explain it in simple words?",
        "Give me one real-world example.",
    ]

    for index, question in enumerate(questions, start=1):
        print("\n" + "=" * 60)
        print(f"QUESTION {index}")
        print("=" * 60)
        print(question)

        response = orchestrator.execute(question)

        print("\nAI-KOS RESPONSE\n")
        print(response)


if __name__ == "__main__":
    main()