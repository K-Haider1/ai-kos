# AI-KOS Architecture

## High-Level Flow

User
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

### Planner Agent

Responsible for:

* Query Understanding
* Task Planning
* Workflow Routing

### Retriever Agent

Responsible for:

* Semantic Search
* Knowledge Retrieval
* Context Selection

### Validator Agent

Responsible for:

* Source Validation
* Confidence Scoring
* Consistency Checks

### Report Generator

Responsible for:

* Summary Creation
* Action Plan Generation

### Critic Agent

Responsible for:

* Hallucination Detection
* Output Review
* Quality Assurance

## Data Layer

* ChromaDB
* Local Storage

## Embedding Layer

* BAAI/bge-small-en-v1.5

## LLM Layer

* Gemini API
* Ollama (Future)
