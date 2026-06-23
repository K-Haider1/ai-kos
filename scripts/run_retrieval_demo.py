from agents.retriever.retriever_agent import RetrieverAgent

agent = RetrieverAgent()

results = agent.retrieve(
    "What is Artificial Intelligence?"
)

print("\nRetrieved Documents:\n")

for doc in results["documents"][0]:
    print(doc)
    print("-" * 50)