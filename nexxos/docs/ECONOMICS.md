# Economic Intelligence Engine

Tracks profitability and operational efficiency of autonomous operations.

## Metrics

### 1. Cost Tracking

**Components**:
- **Token Cost**: LLM API usage
- **Compute Cost**: CPU/GPU resources
- **Infrastructure Cost**: Hosting, services
- **Tool Cost**: Third-party API calls

**Example**:
```json
{
  "task": "Analyze competitor pricing",
  "duration_seconds": 5.2,
  "costs": {
    "token_cost": 0.0015,
    "compute_cost": 0.10,
    "infrastructure_cost": 0.01,
    "total_cost": 0.1115
  }
}
```

### 2. Revenue Attribution

**Sources**:
- Direct revenue from task execution
- Cost savings from automation
- Revenue protection from risk mitigation
- Opportunity cost avoided

**Example**:
```json
{
  "task": "Price optimization",
  "revenue_impact": {
    "direct_revenue": 250,
    "cost_savings": 50,
    "total_revenue": 300
  }
}
```

### 3. ROI Calculation

**Formula**:
```
ROI = (Revenue - Cost) / Cost * 100%
```

**Example**:
```
Revenue: $300
Cost: $0.11
ROI: (300 - 0.11) / 0.11 * 100% = 272,636%
```

### 4. Agent Efficiency

**Metrics**:
- **Execution Cost**: Average cost per task
- **Revenue per Execution**: Average revenue generated
- **Cost per Minute**: Operational cost rate
- **Efficiency Score**: Revenue / Cost ratio

**Example**:
```json
{
  "agent_id": "pricing_agent",
  "period": "monthly",
  "total_executions": 1250,
  "total_cost": 142.35,
  "total_revenue": 45000,
  "metrics": {
    "average_execution_cost": 0.11,
    "average_revenue": 36.00,
    "cost_per_minute": 0.02,
    "efficiency_score": 316.5
  }
}
```

### 5. Operational ROI

**Calculation**:
```
Operational ROI = (Total Revenue - Total Cost) / Total Cost * 100%
```

**Example**:
```
Monthly Revenue: $45,000
Monthly Cost: $142.35
Monthly ROI: 31,556%
```

## Tracking System

```python
from nexxos.core.economics import EconomicTracker

economics = EconomicTracker(agent_id="pricing_agent")

# Track execution
metrics = economics.track_execution(
    task="Analyze market trends",
    duration=5.2,
    result={"trends": [...]}
)

print(metrics)
# {
#   "timestamp": "2026-06-02T10:00:00Z",
#   "costs": {
#     "token_cost": 0.0015,
#     "compute_cost": 0.10,
#     "infrastructure_cost": 0.01,
#     "total_cost": 0.1115
#   },
#   "revenue": {
#     "estimated_revenue": 250
#   },
#   "roi": {
#     "absolute_roi": 249.89,
#     "roi_percentage": 224,012%
#   }
# }

# Get agent-wide metrics
metrics = economics.get_agent_metrics()
```

## Cost Optimization

**Strategies**:
1. **Batch Processing**: Reduce per-task overhead
2. **Caching**: Avoid redundant API calls
3. **Model Selection**: Use cheaper models for simple tasks
4. **Rate Limiting**: Control API usage

## Dashboard Metrics

For NexxSight dashboard:

```json
{
  "time_period": "2026-06-01 to 2026-06-02",
  "agents": [
    {
      "agent_id": "pricing_agent",
      "executions": 1250,
      "total_cost": 142.35,
      "total_revenue": 45000,
      "roi_percentage": 31556,
      "status": "high_efficiency"
    },
    {
      "agent_id": "support_agent",
      "executions": 450,
      "total_cost": 52.15,
      "total_revenue": 8000,
      "roi_percentage": 15235,
      "status": "healthy"
    }
  ],
  "platform_totals": {
    "total_executions": 1700,
    "total_cost": 194.50,
    "total_revenue": 53000,
    "roi_percentage": 27255
  }
}
```

## Billing Integration

Economic data feeds into:
- **Cost Center Allocation**: Charge to departments
- **Chargeback Model**: Internal billing
- **Budget Tracking**: Monitor spend vs budget
- **Capacity Planning**: Right-size infrastructure
