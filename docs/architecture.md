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

* Gemini API (Phase 9)
* Ollama (Future)
* OpenAI Compatible Models (Future)


## Future Frontend

* Angular Dashboard
* Chat Interface
* Analytics
* Document Management
* Multi-Agent Visualization
