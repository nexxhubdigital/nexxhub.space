# Memory Architecture

NexxOS uses a hybrid memory system to create institutional intelligence.

## Memory Layers

### 1. Short-Term Memory (Redis)

**Purpose**: Cache active tasks and recent context

**Stores**:
- Current task state
- Recent interaction history
- Temporary execution cache
- Session context

**Access Pattern**: Microseconds (in-memory)

**Lifespan**: Hours to days

Example:
```json
{
  "execution:exec_123": {
    "task": "Analyze competitor pricing",
    "result": {...},
    "duration": 5.2,
    "timestamp": "2026-06-02T10:00:00Z"
  }
}
```

### 2. Semantic Memory (PostgreSQL + pgvector)

**Purpose**: Long-term knowledge base with semantic search

**Stores**:
- Company knowledge base
- Standard operating procedures
- Operational patterns
- Customer interaction history
- Best practices

**Access Pattern**: Milliseconds (indexed)

**Query Method**: Vector similarity search

Example:
```sql
SELECT * FROM knowledge_base
WHERE embedding <-> query_embedding < 0.1
ORDER BY similarity DESC
LIMIT 10;
```

### 3. Graph Memory (Neo4j)

**Purpose**: Relationship mapping and organizational intelligence

**Stores**:
- Agent relationships
- Organizational structure
- Dependency graphs
- Decision chains
- Workflow relationships

**Access Pattern**: Graph traversal

**Query**: Cypher

Example:
```cypher
MATCH (a:Agent)-[:EXECUTED]->(t:Task)-[:DEPENDS_ON]->(other:Task)
RETURN a, t, other
```

### 4. Strategic Memory (PostgreSQL)

**Purpose**: Persistent business goals and policies

**Stores**:
- Strategic goals
- Policies
- Constraints
- Long-term objectives

**Access Pattern**: SQL queries

Example:
```json
{
  "goal": "Increase ecommerce conversion by 12%",
  "priority": "high",
  "deadline": "2026-Q3",
  "assigned_departments": ["marketing", "pricing"],
  "status": "in_progress"
}
```

## Memory Controller

The `MemoryController` coordinates access across all memory layers:

```python
memory = MemoryController(agent_id="agent_123")

# Load all relevant context
context = memory.load_context(task="Analyze market trends")

# Context includes:
# - short_term_context: Recent task history
# - semantic_context: Relevant knowledge
# - graph_context: Organizational relationships
# - strategic_context: Business goals

# Store execution across all layers
memory.store_execution(
    execution_id="exec_123",
    task="Analyze market trends",
    result={"trends": [...]},
    duration=5.2,
    economic_data={...}
)
```

## Information Flow

```
Agent Task
    ↓
MemoryController.load_context()
    ↓
├─ Short-term: Recent cache
├─ Semantic: Knowledge search
├─ Graph: Relationships
└─ Strategic: Goals context
    ↓
Execution with Full Context
    ↓
Store Results
    ↓
├─ Short-term: Update cache
├─ Semantic: Extract learnings
├─ Graph: Update relationships
└─ Strategic: Track goal progress
```

## Implementation Roadmap

**Phase 1** (Current):
- Redis integration for short-term
- PostgreSQL table schema for semantic
- Neo4j connection pool
- Strategic memory schema

**Phase 2**:
- Vector embedding pipeline
- Semantic search implementation
- Graph query optimization
- Memory synchronization

**Phase 3**:
- Advanced analytics on memory
- Memory compression/archival
- Cross-memory transactions
- Distributed memory nodes
