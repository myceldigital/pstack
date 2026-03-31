# Training Materials: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**Audience:** Regional planners, buyers, logistics approvers, supply-chain leaders

## Training Package Summary

| Asset | Audience | Purpose | Status |
|-------|----------|---------|--------|
| Planner quickstart | planners | daily risk-queue triage and order drilldown workflow | Ready |
| Buyer escalation guide | procurement ops | supplier-delay response and note capture | Ready |
| Approver runbook | logistics + finance approvers | expedite approval and audit trail handling | Draft |
| Executive readout guide | leadership | interpret wallboard without misusing it as operator UI | Ready |

## Operator Workflow Guide

| Workflow | Trigger | Steps | Escalation |
|----------|---------|-------|------------|
| Triage high-risk order | risk score >= 80 or customer priority = platinum | open risk queue, review causality timeline, validate freshness, assign owner or create request | planning manager if confidence low |
| Escalate supplier | supplier root cause with no same-day recovery | open supplier triage page, add contact note, tag buyer owner, set due-by | procurement director for tier-1 suppliers |
| Submit expedite request | approved business need after triage | open approval flow, select request type, enter cost code and reason, submit for logistics review | logistics lead + finance owner |

## Support Runbook

| Scenario | First responder | Diagnostic steps | Escalate to |
|----------|-----------------|------------------|-------------|
| Stale shipment data | planner support lead | check freshness badge, inspect TMS ingest state, compare EDI landing time | platform engineer |
| Missing supplier update | procurement ops lead | verify file arrival, check confidence downgrade, contact supplier | supplier portal owner |
| Approval-page error | logistics systems analyst | verify OSDK auth, inspect finance code list, retry with pilot code | OSDK developer |

## Adoption Risks

| Risk | Likely audience | Mitigation |
|------|------------------|------------|
| planners keep spreadsheet as source of truth | regional planners | first-week office hours plus side-by-side KPI reconciliation |
| executives demand more custom wallboard slices before workflow stabilizes | leadership | position Slate as read-only, not scope-setting |
| buyers skip note capture and revert to email only | procurement ops | require note capture in day-one training and manager review |

## Next Steps

1. [ ] Validate materials against the actual deployed workflow after canary launch.
2. [ ] Hand off ownership of planner and approver materials to the supply excellence PMO.
3. [ ] Capture adoption questions and workarounds for the retro.
