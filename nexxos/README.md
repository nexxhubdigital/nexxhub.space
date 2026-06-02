# NexxOS - Infrastructure for Autonomous Enterprises

NexxOS is an AI-native operational infrastructure platform built on Swarms AI orchestration. It provides enterprise governance, persistent organizational memory, observability, economic intelligence, and operational reliability for autonomous systems.

## Phase 1: Foundation (Current)

Building the operational core with:
- Swarms integration layer
- Memory system
- Logging framework
- Governance middleware
- Agent wrapper architecture

## Project Structure

```
nexxos/
├── core/
│   ├── orchestration/      # Swarms integration layer
│   ├── governance/         # Policy & approval engine
│   ├── economics/          # Cost tracking & ROI
│   ├── observability/      # Logging & monitoring
│   ├── memory/             # Hybrid memory system
│   ├── security/           # Zero-trust model
│   ├── execution/          # Execution engine
│   └── routing/            # Task routing logic
├── agents/                 # Domain-specific agents
├── workflows/              # Workflow definitions
├── dashboards/             # Frontend observability
├── api/                    # REST/GraphQL APIs
├── infrastructure/         # Deployment configs
├── integrations/           # Third-party integrations
├── tests/                  # Test suite
└── docs/                   # Documentation
```

## Stack

| Component | Technology |
|-----------|-----------|
| Runtime | Python 3.11+ |
| Orchestration | Swarms |
| API | FastAPI |
| Queue | RabbitMQ / Kafka |
| Cache | Redis |
| DB (Relational) | PostgreSQL |
| DB (Graph) | Neo4j |
| DB (Vector) | pgvector / Qdrant |
| Deployment | Kubernetes |
| Monitoring | OpenTelemetry |
| Dashboard | React + Next.js |

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run core services
docker-compose up -d

# Initialize database
python -m nexxos.core.setup

# Start development server
python -m nexxos.api.main
```

## Documentation

- [Architecture](./docs/ARCHITECTURE.md)
- [Core Components](./docs/CORE_COMPONENTS.md)
- [Memory System](./docs/MEMORY.md)
- [Governance](./docs/GOVERNANCE.md)
- [Economics](./docs/ECONOMICS.md)
