# AI-KOS Architecture

---

# High-Level System Architecture

```
                        +----------------------+
                        |      User Query      |
                        +----------+-----------+
                                   |
                                   v
                     +----------------------------+
                     |    Orchestrator Service     |
                     +--------------+-------------+
                                    |
                                    v
                          +-------------------+
                          |  Planner Agent    |
                          +---------+---------+
                                    |
                 +------------------+------------------+
                 |                                     |
                 |                                     |
         Knowledge Query                      General Query
                 |                                     |
                 v                                     v
          +--------------+                 +------------------+
          | RAG Service  |                 |  LLM Provider    |
          +------+-------+                 +------------------+
                 |
                 v
        +------------------+
        | Retriever Agent  |
        +--------+---------+
                 |
                 v
      +------------------------+
      | ChromaDB Vector Store  |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Retrieved Documents    |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Validator Agent        |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Context Builder        |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Prompt Builder         |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Gemini Provider        |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Report Generator       |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Critic Agent           |
      +-----------+------------+
                  |
                  v
      +------------------------+
      | Final Approved Answer  |
      +------------------------+
```

---

# Document Ingestion Flow

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
Chunker
    │
    ▼
Embedding Service
    │
    ▼
ChromaDB Vector Store
```

---

# Retrieval Flow

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

# End-to-End RAG Flow

```
User Query
      │
      ▼
Planner Agent
      │
      ▼
Knowledge Query?
      │
      ▼
RAG Service
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
Prompt Builder
      │
      ▼
LLM Provider Factory
      │
      ▼
Gemini Provider
      │
      ▼
Report Generator
      │
      ▼
Critic Agent
      │
      ▼
Final Approved Answer
```

---

# RAG Service Responsibilities

- Validate user query
- Validate top-k
- Retrieve semantic documents
- Remove invalid documents
- Build retrieval context
- Generate prompt
- Route request to configured LLM
- Return grounded answer

---

# Planner Agent

Responsibilities

- Understand user request
- Identify query type
- Route workflow
- Create execution plan

---

# Retriever Agent

Responsibilities

- Semantic Search
- Similarity Matching
- Context Retrieval

---

# Validator Agent

Responsibilities

- Remove invalid documents
- Normalize retrieved content
- Ensure usable context

---

# Context Builder

Responsibilities

- Combine retrieved chunks
- Produce clean context

---

# Prompt Builder

Responsibilities

- Construct grounded prompts
- Prevent hallucination
- Standardize prompting

---

# LLM Provider Layer

Current

- Gemini API

Future

- OpenAI
- Ollama
- Claude
- Azure OpenAI
- AWS Bedrock

---

# Report Generator

Responsibilities

- Format generated answer
- Create structured output

---

# Critic Agent

Responsibilities

- Review generated answer
- Detect obvious hallucinations
- Approve final response

---

# Data Layer

- ChromaDB
- Persistent Storage

---

# Embedding Layer

- BAAI/bge-small-en-v1.5

---

# Future AI-KOS Roadmap

- LangGraph
- Multi-Agent Graph Execution
- Human-in-the-loop
- Memory
- Checkpointing
- Tool Calling
- Web Search
- SQL Agent
- Vision Models
- Evaluation Pipeline
- Monitoring
- Observability
- Angular Dashboard
- Analytics