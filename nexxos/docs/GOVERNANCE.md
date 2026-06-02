# Governance Engine

The Governance Engine prevents dangerous or uncontrolled autonomous execution.

## Components

### 1. Policy Engine

Defines and enforces permissions.

**Controls**:
- Agent permissions
- Execution scope
- Financial limits
- API access
- Workflow authorization

**Policy Example**:
```yaml
policies:
  pricing_agent:
    permissions:
      - read_products
      - read_competitor_data
      - update_prices
    financial_limits:
      daily_spend: 100
      single_transaction: 50
    api_rate_limits:
      requests_per_minute: 100
    requires_approval_for:
      - price_change_exceeds_10_percent
      - price_change_affects_top_100_products
```

### 2. Risk Scoring

Multidimensional risk assessment.

**Dimensions**:
- **Financial Risk** (40%): Cost, refunds, price changes
- **Security Risk** (30%): Data access, API calls
- **Operational Risk** (20%): Availability, performance
- **Compliance Risk** (10%): Regulatory, audit

**Example**:
```python
risk_score = (
    0.4 * financial_risk +
    0.3 * security_risk +
    0.2 * operational_risk +
    0.1 * compliance_risk
)

# 0.0 = No risk (approved)
# 0.5 = Medium risk (requires manager approval)
# 0.8+ = High risk (requires executive approval)
```

### 3. Approval System

Routes tasks to appropriate approvers.

**Approval Matrix**:

| Action | Risk | Approver | SLA |
|--------|------|----------|-----|
| Update price (< 5%) | Low | Auto-approve | Immediate |
| Update price (5-10%) | Medium | Department Lead | 1 hour |
| Update price (> 10%) | High | VP | 4 hours |
| Refund customer | Medium | Finance | 2 hours |
| Delete customer data | High | Legal + Security | 24 hours |

**Approval Flow**:
```
Task submitted
    ↓
Risk scored
    ↓
If risk < threshold → Auto-approved
Else → Route to appropriate approver
    ↓
Approver notified (email, dashboard)
    ↓
Approval decision recorded
    ↓
Execution or rejection
```

### 4. Audit Logging

Complete audit trail for compliance.

**Logged Events**:
- Task submission
- Policy checks
- Risk score
- Approval requests
- Approval decisions
- Execution start
- Execution result
- Any modifications

**Audit Entry**:
```json
{
  "timestamp": "2026-06-02T10:00:00Z",
  "agent": "pricing_agent",
  "action": "price_change",
  "old_price": 40,
  "new_price": 45,
  "reason": "competitor price increase",
  "risk_score": 0.35,
  "governance_check": "approved",
  "approver": "auto",
  "execution_id": "exec_123",
  "result": "success"
}
```

## Usage

```python
from nexxos.core.governance import GovernanceMiddleware

gov = GovernanceMiddleware(agent_id="pricing_agent")

# Validate task
check = gov.validate(
    task="Update price from $40 to $45",
    agent_id="pricing_agent",
    department="ecommerce"
)

print(check)
# {
#   "allowed": true,
#   "risk_score": 0.35,
#   "requires_approval": false,
#   "timestamp": "2026-06-02T10:00:00Z"
# }

# If approval needed, request it
if check["requires_approval"]:
    approval = gov.request_approval(
        task="Update price from $40 to $45",
        risk_score=check["risk_score"],
        agent_id="pricing_agent"
    )
```

## Security Guarantees

1. **No execution without validation**: All tasks checked
2. **Deterministic decisions**: Policies applied consistently
3. **Complete auditability**: Every action logged
4. **Escalation**: High-risk tasks reach appropriate humans
5. **Compliance**: Audit trail for regulatory requirements
