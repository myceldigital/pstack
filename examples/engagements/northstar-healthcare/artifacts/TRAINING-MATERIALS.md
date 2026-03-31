# Training Materials: Northstar Healthcare Patient Flow

**Date:** 2026-03-31  
**Audience:** Capacity nurses, transfer center coordinators, care management, nursing leaders, throughput executives

## Training Package Summary

| Asset | Audience | Purpose | Status |
|-------|----------|---------|--------|
| Command-center quickstart | capacity nurses | ranked queue, bed match, and barrier triage | Ready |
| Transfer center runbook | transfer coordinators | acknowledgment and escalation workflow | Ready |
| Care-management barrier guide | case management + EVS leads | discharge barrier ownership and escalation | Ready |
| Executive throughput deck | leadership | how to interpret aggregate capacity surfaces | Ready |

## Operator Workflow Guide

| Workflow | Trigger | Steps | Escalation |
|----------|---------|-------|------------|
| Assign next bed | patient rises to top of queue | review placement rationale, confirm staffed bed, assign owner, notify unit | nursing supervisor if confidence low |
| Escalate discharge barrier | barrier aging breaches threshold | open barrier board, review owner team, add reason, escalate | unit director or EVS supervisor |
| Acknowledge transfer request | transfer center asks for site decision | open console, review current barriers and bed options, acknowledge and route | throughput supervisor for urgent ICU cases |

## Support Runbook

| Scenario | First responder | Diagnostic steps | Escalate to |
|----------|-----------------|------------------|-------------|
| Stale staffing data | command-center super user | inspect freshness banner, confirm Kronos file arrival, compare unit staffing board | nursing ops analyst |
| Missing EVS barrier | EVS lead | verify room state, inspect EVS export, create manual task if absent | platform engineer |
| Transfer console error | transfer-center analyst | verify auth and duplicate-ack state, retry idempotent action | OSDK developer |

## Adoption Risks

| Risk | Likely audience | Mitigation |
|------|------------------|------------|
| command-center staff keep relying on phone tree first | nurses and coordinators | shadow shifts plus queue-based huddle facilitation |
| leaders ask for patient-identifiable wallboard content | executives | enforce aggregate-only policy and training |
| care-management teams underuse barrier ownership | case management | manager review of aging unowned barriers |

## Next Steps

1. [ ] Validate materials against the deployed workflow after first pilot shift.
2. [ ] Hand off ownership of each asset to command-center operations leadership.
3. [ ] Capture adoption and confidence issues for the retro.
