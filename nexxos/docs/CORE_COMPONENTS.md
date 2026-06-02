# Core Components

## NexxAgent

Wrapper around Swarms Agent that integrates all NexxOS capabilities.

```python
from nexxos.core.orchestration import NexxAgent

agent = NexxAgent(
    agent_config={
        "name": "pricing_agent",
        "model": "gpt-4",
        "tools": [pricing_tool],
    },
    department="ecommerce",
    role="analyst"
)

result = agent.run(
    task="Analyze competitor pricing and recommend adjustments",
    require_approval=True
)
```

## GovernanceMiddleware

Enforces policies before agent execution.

Features:
- Policy validation
- Risk scoring
- Approval routing
- Audit logging

```python
from nexxos.core.governance import GovernanceMiddleware

governance = GovernanceMiddleware(agent_id="pricing_agent")

check = governance.validate(
    task="Update product prices",
    agent_id="pricing_agent",
    department="ecommerce"
)

if check["requires_approval"]:
    approval = governance.request_approval(
        task="Update product prices",
        risk_score=check["risk_score"],
        agent_id="pricing_agent"
    )
```

## MemoryController

Orchestrates hybrid memory system.

```python
from nexxos.core.memory import MemoryController

memory = MemoryController(agent_id="pricing_agent")

# Load context for task
context = memory.load_context("Adjust prices based on demand")

# Store execution results
memory.store_execution(
    execution_id="exec_123",
    task="Adjust prices",
    result={"new_prices": {...}},
    duration=5.2,
    economic_data={...}
)
```

## EconomicTracker

Tracks costs and ROI.

```python
from nexxos.core.economics import EconomicTracker

economics = EconomicTracker(agent_id="pricing_agent")

metrics = economics.track_execution(
    task="Analyze competitor pricing",
    duration=5.2,
    result={"analysis": "..."}
)

print(f"ROI: {metrics['roi']['roi_percentage']}%")
```

## TelemetryCollector

Records execution events.

```python
from nexxos.core.observability import TelemetryCollector

telemetry = TelemetryCollector(agent_id="pricing_agent")

telemetry.record_execution(
    execution_id="exec_123",
    task="Analyze pricing",
    result={"analysis": "..."},
    duration=5.2,
    governance_check=governance_result,
    economic_data=economics_result
)
```
