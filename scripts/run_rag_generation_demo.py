"""
End-to-End RAG Generation Demo
Author: Kahkashan Haider
"""

from services.rag_service import RAGService


def main():

    rag_service = RAGService()

    question = "What is Retrieval-Augmented Generation?"

    print("\nUSER QUESTION:\n")
    print(question)

    answer = rag_service.generate_answer(
        query=question,
        top_k=3,
    )

    print("\nAI-KOS ANSWER:\n")
    print(answer)


if __name__ == "__main__":
    main()