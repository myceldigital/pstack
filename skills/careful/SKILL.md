---
name: careful
version: 1.0.0
description: |
  Warn before destructive operations on customer Foundry environments.
  Blocks ontology deletions, pipeline overwrites, permission changes,
  and data purges without explicit DS confirmation.
  Use when working in production customer environments. (pstack)
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# Careful Mode

When active, require explicit DS confirmation before ANY of these operations:

## Destructive Operations — ALWAYS CONFIRM

```
Ontology:
- Delete object type
- Remove property from object type
- Delete link type
- Remove action type
- Change primary key of object type
- Change backing dataset of object type

Pipelines:
- Delete dataset
- Overwrite raw dataset with transformed data
- Change build schedule of production pipeline
- Delete pipeline transform
- Modify incremental pipeline checkpoint

Workshop:
- Delete application
- Remove page from published application
- Change action binding on production button
- Modify event wiring on published app

AIP:
- Delete agent
- Modify system prompt of production agent
- Change tool configuration of production agent
- Remove context source from production agent
- Modify Automate workflow trigger

Permissions:
- ANY change to ontology permissions
- ANY change to marking configuration
- ANY change to OSDK application scopes
- ANY change to agent access scoping

Apollo:
- Trigger production deployment
- Rollback production deployment
- Change release channel subscription
```

## Confirmation Format

Before executing any destructive operation:

```
⚠️ CAREFUL MODE — Destructive operation detected

Operation: [What will happen]
Target: [What will be affected]
Reversible: [Yes — how to undo / No — permanent]
Impact: [What downstream systems/users are affected]

Are you sure you want to proceed?
A) Yes, proceed
B) No, cancel
C) Show me what will change first
```

NEVER proceed without explicit "Yes" confirmation from the DS.

## Activation

Careful mode is active when:
- The DS invokes `/careful`
- The DS invokes `/guard` (which activates both careful + freeze)
- Working in a production customer environment (auto-detect)

Careful mode is deactivated when:
- The DS explicitly says "deactivate careful mode"
- The session ends
