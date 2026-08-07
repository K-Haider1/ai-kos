# AI-KOS Architecture

---

# Overview

AI-KOS is a modular Retrieval-Augmented Generation (RAG) platform designed with a multi-agent architecture.

The system combines document retrieval, large language models, conversation memory, planning, validation, and response review into a production-ready AI pipeline.

---

# High-Level Architecture

```
                        User
                         │
                         ▼
              Orchestrator Service
                         │
                         ▼
                  Planner Agent
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
  Knowledge Query               General Query
          │                             │
          ▼                             ▼
      RAG Service                 LLM Provider
          │                             │
          ▼                             │
  Retriever Agent                       │
          │                             │
          ▼                             │
  Validator Agent                       │
          │                             │
          ▼                             │
  Context Builder                       │
          │                             │
          ▼                             │
 History Formatter                      │
          │                             │
          ▼                             │
   Prompt Builder                       │
          │                             │
          └──────────────┬──────────────┘
                         ▼
                   LLM Provider
                         │
                         ▼
                Report Generator
                         │
                         ▼
                   Critic Agent
                         │
                         ▼
                 Memory Service
                         │
                         ▼
             Conversation Memory
                         │
                         ▼
                 Final Response
```

---

# Document Ingestion Pipeline

```
Document
   │
   ▼
PDF Loader
   │
   ▼
Text Cleaner
   │
   ▼
Text Chunker
   │
   ▼
Embedding Service
   │
   ▼
ChromaDB Vector Store
```

---

# Retrieval Pipeline

```
User Query
     │
     ▼
Retriever Agent
     │
     ▼
Embedding Service
     │
     ▼
Vector Search
     │
     ▼
Top-K Documents
```

---

# RAG Pipeline

```
User Query
     │
     ▼
Retriever Agent
     │
     ▼
Validator Agent
     │
     ▼
Context Builder
     │
     ▼
History Formatter
     │
     ▼
Prompt Builder
     │
     ▼
LLM Provider
     │
     ▼
Generated Answer
```

---

# Conversation Memory Pipeline

```
User Question
      │
      ▼
Memory Service
      │
      ▼
Conversation Memory
      │
      ▼
History Formatter
      │
      ▼
Prompt Builder
      │
      ▼
LLM Response
      │
      ▼
Save Interaction
```

---

# Components

## Planner Agent

Responsibilities

- Classify user queries
- Determine execution strategy
- Create execution plans

---

## Retriever Agent

Responsibilities

- Semantic search
- Similarity retrieval
- Top-K document retrieval

---

## Validator Agent

Responsibilities

- Remove invalid documents
- Normalize retrieved content
- Ensure high-quality context

---

## Context Builder

Responsibilities

- Merge retrieved chunks
- Produce retrieval context

---

## History Formatter

Responsibilities

- Format previous conversations
- Ignore invalid interactions
- Produce prompt-ready history

---

## Prompt Builder

Responsibilities

- Combine conversation history
- Combine retrieved knowledge
- Add current user question
- Generate standardized prompts

---

## LLM Provider Layer

Current Provider

- Google Gemini

Future Providers

- OpenAI
- Claude
- Ollama
- Azure OpenAI
- AWS Bedrock

---

## Report Generator

Responsibilities

- Generate structured response objects

Response format

```python
{
    "query": "...",
    "answer": "...",
    "status": "approved"
}
```

---

## Critic Agent

Responsibilities

- Review generated responses
- Validate report structure
- Approve final response

---

## Memory Service

Responsibilities

- Save conversations
- Retrieve conversations
- Clear conversations

Current implementation

- In-memory storage

Future implementations

- SQLite
- Redis
- ChromaDB

---

# Data Layer

Vector Database

- ChromaDB

Embedding Model

- BAAI/bge-small-en-v1.5

---

# Current System Features

✅ Document Ingestion

✅ Semantic Search

✅ Retrieval-Augmented Generation

✅ Planner-based Routing

✅ Conversation Memory

✅ History-aware Prompt Generation

✅ Structured Report Generation

✅ Critic Review

✅ Modular Architecture

✅ Provider Abstraction

---

# Current AI Agents

- Planner Agent
- Retriever Agent
- Validator Agent
- Report Generator Agent
- Critic Agent

---

# Current Services

- Embedding Service
- Context Builder
- Prompt Builder
- RAG Service
- Memory Service
- Orchestrator Service

---

# Testing

The project includes

- Unit Tests
- Integration Tests
- End-to-End Tests

Current Status

57 / 57 Tests Passing