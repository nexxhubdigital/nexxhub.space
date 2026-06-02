"""Short-Term Memory

Redis-backed cache for active tasks and recent interactions.
"""

from typing import Any, Dict, Optional


class ShortTermMemory:
    """
    Redis-backed short-term memory.

    Stores:
    - Active task state
    - Recent interactions
    - Temporary context
    """

    def __init__(self):
        # TODO: Initialize Redis connection
        pass

    def retrieve(self, query: str) -> Dict[str, Any]:
        """Retrieve recent context."""
        # TODO: Query Redis
        return {}

    def store(self, key: str, value: Any) -> None:
        """Store temporary data."""
        # TODO: Write to Redis
        pass

    def clear(self) -> None:
        """Clear cache."""
        # TODO: Flush Redis cache
        pass
