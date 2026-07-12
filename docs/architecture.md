# AI-KOS Architecture

## Document Ingestion Flow

Document
↓
Loader
↓
Text Cleaner
↓
Chunker
↓
Embedding Service
↓
ChromaDB Vector Store

## Retrieval Flow

User Query
↓
Retriever Agent
↓
Embedding Service
↓
ChromaDB Vector Store
↓
Relevant Context

## Multi-Agent Flow (Future)

User Query
↓
Planner Agent
↓
Retriever Agent
↓
Validator Agent
↓
Report Generator
↓
Critic Agent
↓
Final Response

## Context Generation Flow

User Question
↓
Retriever Agent
↓
Top-K Retrieved Chunks
↓
Context Builder
↓
Prompt Builder
↓
LLM Ready Prompt

## RAG Generation Pipeline

User Query
↓
RAG Service
↓
Retriever Agent
↓
Embedding Service
↓
ChromaDB Vector Store
↓
Retrieved Documents
↓
Context Builder
↓
Prompt Builder
↓
LLM Provider Factory
↓
Configured LLM Provider
↓
Grounded Final Answer

### RAG Service Responsibilities

- Validate user queries
- Validate retrieval parameters
- Retrieve relevant knowledge
- Filter empty or invalid documents
- Prevent LLM calls when no usable context exists
- Build grounded context
- Generate prompts
- Route requests through the configured LLM provider
- Return the final generated answer

## Components

### Retriever Agent

* Semantic Search
* Context Retrieval
* Knowledge Lookup

### Planner Agent

* Task Planning
* Workflow Routing

### Validator Agent

* Fact Validation
* Confidence Scoring

### Report Generator

* Summary Generation
* Action Plans

### Critic Agent

* Hallucination Detection
* Quality Review

## Data Layer

* ChromaDB
* Local Storage

## Embedding Layer

* BAAI/bge-small-en-v1.5

## LLM Layer

* Gemini API (Current Default Provider)
* Ollama (Future)
* OpenAI Compatible Models (Future)


## Future Frontend

* Angular Dashboard
* Chat Interface
* Analytics
* Document Management
* Multi-Agent Visualization
