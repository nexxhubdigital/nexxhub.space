"""Orchestration Layer

Wrapper architecture around Swarms for:
- Agent execution
- Task routing
- Concurrency management
- Tool execution
- Runtime control
"""

from .agent_wrapper import NexxAgent
from .task_router import TaskRouter
from .execution_engine import ExecutionEngine

__all__ = ["NexxAgent", "TaskRouter", "ExecutionEngine"]
