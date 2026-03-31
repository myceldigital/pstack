---
name: freeze
version: 1.0.0
description: |
  Lock edits to a specific Foundry project scope. Prevents agents from
  modifying resources outside the designated project boundary.
  Use when working on a specific customer project to prevent cross-contamination. (pstack)
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# Freeze Mode

When active, restrict ALL modifications to resources within a specified scope.

## Configuration

When invoked, ask the DS:

```
What scope should I restrict to?

A) Specific Foundry project: [project path]
B) Specific use case: [only resources tagged for use case N]
C) Specific environment: [dev / staging / production]
D) Custom scope: [DS specifies exact boundaries]
```

## Enforcement

When freeze mode is active:

```
ALLOWED:
- Read any resource (read-only access is unrestricted)
- Modify resources WITHIN the frozen scope
- Create new resources WITHIN the frozen scope

BLOCKED:
- Modify resources OUTSIDE the frozen scope
- Delete resources OUTSIDE the frozen scope
- Change permissions on resources OUTSIDE the frozen scope

If an agent attempts to modify an out-of-scope resource:
"🧊 FREEZE MODE — This resource is outside the frozen scope.
Scope: [current scope]
Attempted: [what was attempted]
Resource: [what resource]
To modify this resource, either change the freeze scope or deactivate freeze mode."
```

## Deactivation

```
/unfreeze — removes scope restriction
DS says "deactivate freeze" — removes scope restriction
Session ends — freeze mode deactivates
```
