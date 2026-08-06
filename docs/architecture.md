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

## Conversation Memory Layer

The Conversation Memory Layer enables AI-KOS to remember recent
interactions during a session.

### Components

#### ConversationMemory

Responsible for:

- Storing user interactions
- Returning recent conversations
- Clearing session memory
- Validating stored data

#### MemoryService

Provides a service layer over ConversationMemory.

Responsibilities:

- Save conversations
- Retrieve recent history
- Clear memory
- Hide memory implementation details from other modules

Current Storage:

- In-memory (Python list)

Future Storage:

- SQLite
- ChromaDB
- Redis

# Planner Agent
* Query Classification
* Task Planning
* Workflow Routing
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
### Conversation Memory

* Session Memory
* Conversation History
* Recent Interaction Retrieval

### Memory Service

* Memory Management
* Save Conversations
* Retrieve Conversations
* Clear Memory

# Data Layer

- ChromaDB
- Persistent Storage

---

# Embedding Layer

- BAAI/bge-small-en-v1.5

---

# Future AI-KOS Roadmap
## Multi-Agent Orchestration Flow

User Query
↓
Planner Agent
↓
Memory Service
↓
Conversation Memory
↓
Workflow Routing
↓
Retriever Agent / LLM
↓
Report Generator
↓
Critic Agent
↓
Memory Update
↓
Final Response

### Orchestrator Responsibilities

- Receive user queries
- Create an execution plan using the Planner Agent
- Retrieve recent conversation history
- Route knowledge queries through the RAG pipeline
- Route general queries directly to the configured LLM
- Generate a structured report
- Review the report using the Critic Agent
- Save the approved interaction into conversation memory
- Return the final reviewed response