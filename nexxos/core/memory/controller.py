"""Memory Controller

Orchestrates access to hybrid memory systems.

Manages:
- Context loading for task execution
- Memory persistence
- Cross-memory synchronization
"""

import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class MemoryController:
    """
    Central controller for hybrid memory architecture.

    Coordinates:
    - Short-term memory (Redis)
    - Long-term semantic memory (PostgreSQL + pgvector)
    - Graph memory (Neo4j)
    - Strategic memory (PostgreSQL)
    """

    def __init__(self, agent_id: str):
        """Initialize memory controller for an agent."""
        self.agent_id = agent_id
        self._short_term = None
        self._semantic = None
        self._graph = None
        self._strategic = None

    @property
    def short_term(self):
        """Lazy-load short-term memory (Redis)."""
        if self._short_term is None:
            from .short_term import ShortTermMemory

            self._short_term = ShortTermMemory()
        return self._short_term

    @property
    def semantic(self):
        """Lazy-load semantic memory (PostgreSQL + pgvector)."""
        if self._semantic is None:
            from .semantic import SemanticMemory

            self._semantic = SemanticMemory()
        return self._semantic

    @property
    def graph(self):
        """Lazy-load graph memory (Neo4j)."""
        if self._graph is None:
            from .graph import GraphMemory

            self._graph = GraphMemory()
        return self._graph

    @property
    def strategic(self):
        """Lazy-load strategic memory (PostgreSQL)."""
        if self._strategic is None:
            from .strategic import StrategicMemory

            self._strategic = StrategicMemory()
        return self._strategic

    def load_context(self, task: str) -> Dict[str, Any]:
        """
        Load contextual information for task execution.

        Retrieves:
        - Recent task history (short-term)
        - Relevant company knowledge (semantic)
        - Organizational context (graph)
        - Strategic goals (strategic)
        """
        logger.info(f"Loading execution context for task: {task}")

        context = {
            "task": task,
            "agent_id": self.agent_id,
            "short_term_context": self.short_term.retrieve(task),
            "semantic_context": self.semantic.retrieve(task),
            "graph_context": self.graph.retrieve(task),
            "strategic_context": self.strategic.retrieve(task),
        }

        return context

    def store_execution(
        self,
        execution_id: str,
        task: str,
        result: Dict[str, Any],
        duration: float,
        economic_data: Dict[str, Any],
    ) -> None:
        """
        Persist execution data across memory layers.

        Stores:
        - Short-term: Recent execution cache
        - Semantic: Extracted learnings and patterns
        - Graph: Execution relationships
        - Strategic: Impact on goals
        """
        logger.info(f"Storing execution {execution_id}")

        # Store in short-term
        self.short_term.store(
            key=f"execution:{execution_id}",
            value={
                "task": task,
                "result": result,
                "duration": duration,
                "economic_data": economic_data,
            },
        )

        # Extract and store semantic knowledge
        self.semantic.store(
            execution_id=execution_id,
            task=task,
            result=result,
        )

        # Update graph relationships
        self.graph.add_execution(
            execution_id=execution_id,
            agent_id=self.agent_id,
            task=task,
        )

        logger.info(f"Execution {execution_id} persisted across memory layers")

    def retrieve_history(self, limit: int = 100) -> list:
        """Retrieve agent execution history."""
        # TODO: Aggregate execution history from semantic memory
        return []

    def clear_short_term(self) -> None:
        """Clear short-term memory cache."""
        self.short_term.clear()
