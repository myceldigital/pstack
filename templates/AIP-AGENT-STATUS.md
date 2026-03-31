# AIP Agent Status Template

**Usage:** Produced by `/aip-architect`. Consumed by `/foundry-reviewer`, `/foundry-security`, `/foundry-qa`.

---

# AIP Agent Status: [Customer Name]

**Date:** [YYYY-MM-DD]
**Upstream:** `ONTOLOGY-ARCHITECTURE.md`, `WORKSHOP-BUILD-STATUS.md`

## Agent Summary

| Agent | Primary job | Context scope | Tools | Status | Eval status |
|-------|-------------|---------------|-------|--------|-------------|
| [Ops copilot] | [explain risk + recommend action] | [Shipment, Supplier] | [search, action stub] | [GREEN/AMBER/RED] | [Pass/Fail] |

## Prompt And Tooling Decisions

| Area | Decision | Risk if wrong | Mitigation |
|------|----------|---------------|------------|
| System prompt | [bounded to expedite workflow] | [scope creep] | [hard guardrail] |
| Tooling | [read-only + confirm-before-action] | [unsafe mutation] | [DS approval] |

## Eval Coverage

| Scenario | Expected behavior | Result | Gap |
|----------|-------------------|--------|-----|
| [High-risk shipment] | [recommend expedite, cite evidence] | [Pass/Fail] | [note] |
| [Prompt injection attempt] | [refuse out-of-scope request] | [Pass/Fail] | [note] |

## Blockers And Decisions

| Blocker | Severity | Security-sensitive? | Needs DS input? |
|---------|----------|---------------------|-----------------|
| [Issue] | [High/Med/Low] | [Yes/No] | [Yes/No] |

## Next Steps

1. [ ] Pass bounded prompt, tool, and eval evidence to security and QA.
2. [ ] Do not widen scope without explicit DS approval.
3. [ ] Keep agent behavior tied to the actual operational decision.
