from agents.retriever.retriever_agent import RetrieverAgent
from services.context_builder import ContextBuilder
from prompts.prompt_builder import PromptBuilder

question = "What is Retrieval Augmented Generation ?"

retriever = RetrieverAgent()

results = retriever.retrieve(
    question, top_k=3
)

documents = results["documents"][0]
context_builder = ContextBuilder()

context = context_builder.build_context(documents)

prompt_builder = PromptBuilder()
prompt = prompt_builder.build_prompt(
    question,
    context
)
print("\nFINAL PROMPT:\n")
print(prompt)
