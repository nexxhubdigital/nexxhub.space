"""NexxAgent Wrapper

Wraps Swarms Agent with NexxOS-specific functionality:
- Governance validation
- Memory integration
- Economic tracking
- Observability hooks
- Execution context management
"""

import logging
from typing import Any, Dict, Optional
from datetime import datetime
import uuid

logger = logging.getLogger(__name__)


class NexxAgent:
    """
    Wrapper around Swarms Agent that integrates:
    - Governance middleware for policy enforcement
    - Memory controller for context persistence
    - Economic tracker for cost/ROI analysis
    - Observability for execution tracking
    """

    def __init__(
        self,
        agent_config: Dict[str, Any],
        agent_id: Optional[str] = None,
        department: Optional[str] = None,
        role: Optional[str] = None,
    ):
        """
        Initialize NexxAgent.

        Args:
            agent_config: Configuration dict for underlying Swarms Agent
            agent_id: Unique identifier for this agent
            department: Organizational department (e.g., "marketing", "finance")
            role: Agent role (e.g., "analyst", "executor", "coordinator")
        """
        self.agent_id = agent_id or str(uuid.uuid4())
        self.department = department
        self.role = role
        self.agent_config = agent_config

        # Lazy imports to avoid hard dependency on swarms
        self._agent = None
        self._governance = None
        self._memory = None
        self._economics = None
        self._telemetry = None

        logger.info(
            f"NexxAgent initialized: {self.agent_id} "
            f"(dept={department}, role={role})"
        )

    @property
    def agent(self):
        """Lazy-load underlying Swarms Agent."""
        if self._agent is None:
            try:
                from swarms import Agent

                self._agent = Agent(**self.agent_config)
            except ImportError:
                raise ImportError(
                    "Swarms not installed. Install with: pip install swarms"
                )
        return self._agent

    @property
    def governance(self):
        """Lazy-load governance middleware."""
        if self._governance is None:
            from nexxos.core.governance import GovernanceMiddleware

            self._governance = GovernanceMiddleware(agent_id=self.agent_id)
        return self._governance

    @property
    def memory(self):
        """Lazy-load memory controller."""
        if self._memory is None:
            from nexxos.core.memory import MemoryController

            self._memory = MemoryController(agent_id=self.agent_id)
        return self._memory

    @property
    def economics(self):
        """Lazy-load economic tracker."""
        if self._economics is None:
            from nexxos.core.economics import EconomicTracker

            self._economics = EconomicTracker(agent_id=self.agent_id)
        return self._economics

    @property
    def telemetry(self):
        """Lazy-load telemetry collector."""
        if self._telemetry is None:
            from nexxos.core.observability import TelemetryCollector

            self._telemetry = TelemetryCollector(agent_id=self.agent_id)
        return self._telemetry

    def run(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None,
        require_approval: bool = False,
    ) -> Dict[str, Any]:
        """
        Execute task with full NexxOS middleware.

        Args:
            task: Task description/prompt
            context: Optional execution context
            require_approval: Whether task requires approval before execution

        Returns:
            Execution result with metadata
        """
        execution_id = str(uuid.uuid4())
        start_time = datetime.utcnow()

        try:
            # Step 1: Governance validation
            logger.info(f"[{execution_id}] Validating task against policies...")
            governance_check = self.governance.validate(
                task=task,
                agent_id=self.agent_id,
                department=self.department,
            )

            if not governance_check["allowed"]:
                logger.warning(
                    f"[{execution_id}] Task blocked by governance: "
                    f"{governance_check['reason']}"
                )
                return {
                    "success": False,
                    "error": "governance_denied",
                    "reason": governance_check["reason"],
                    "execution_id": execution_id,
                }

            # Step 2: Approval system (if required)
            if require_approval:
                logger.info(f"[{execution_id}] Awaiting approval...")
                approval_result = self.governance.request_approval(
                    task=task,
                    risk_score=governance_check.get("risk_score", 0),
                    agent_id=self.agent_id,
                )

                if not approval_result["approved"]:
                    logger.info(
                        f"[{execution_id}] Task approval denied"
                    )
                    return {
                        "success": False,
                        "error": "approval_denied",
                        "execution_id": execution_id,
                    }

            # Step 3: Load contextual memory
            logger.info(f"[{execution_id}] Loading contextual memory...")
            task_context = self.memory.load_context(task)

            # Step 4: Execute via Swarms
            logger.info(f"[{execution_id}] Executing task...")
            result = self.agent.run(task)

            # Step 5: Economic tracking
            end_time = datetime.utcnow()
            duration = (end_time - start_time).total_seconds()
            economic_data = self.economics.track_execution(
                task=task,
                duration=duration,
                result=result,
            )

            # Step 6: Store result in memory
            logger.info(f"[{execution_id}] Persisting execution data...")
            self.memory.store_execution(
                execution_id=execution_id,
                task=task,
                result=result,
                duration=duration,
                economic_data=economic_data,
            )

            # Step 7: Emit telemetry
            self.telemetry.record_execution(
                execution_id=execution_id,
                task=task,
                result=result,
                duration=duration,
                governance_check=governance_check,
                economic_data=economic_data,
            )

            logger.info(f"[{execution_id}] Execution completed successfully")

            return {
                "success": True,
                "execution_id": execution_id,
                "result": result,
                "duration_seconds": duration,
                "economics": economic_data,
                "governance": governance_check,
            }

        except Exception as e:
            logger.error(f"[{execution_id}] Execution failed: {str(e)}", exc_info=True)

            # Record failure
            self.telemetry.record_error(
                execution_id=execution_id,
                task=task,
                error=str(e),
            )

            return {
                "success": False,
                "execution_id": execution_id,
                "error": str(e),
                "duration_seconds": (
                    datetime.utcnow() - start_time
                ).total_seconds(),
            }

    async def run_async(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Async variant of run() for concurrent execution."""
        # Placeholder for async implementation
        raise NotImplementedError("Async execution coming in Phase 2")
