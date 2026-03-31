---
name: guard
version: 1.0.0
description: |
  Activate both careful + freeze at once. Maximum safety for production
  customer environments. Use when entering a live customer Foundry. (pstack)
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---

# Guard Mode

Guard mode activates BOTH careful mode AND freeze mode simultaneously.
This is the maximum safety configuration for working in production
customer environments.

## Activation

When the DS invokes `/guard`:

1. Activate careful mode (all destructive operations require confirmation)
2. Ask for freeze scope (restrict modifications to a specific project/environment)
3. Confirm both are active:

```
🛡️ GUARD MODE ACTIVE

Careful: ✅ All destructive operations require confirmation
Freeze scope: [specified scope]

To deactivate: say "deactivate guard" or end session
```

## Behavior

All rules from `/careful` AND `/freeze` apply simultaneously.
Guard mode is the recommended default for any production customer work.

## Deactivation

- DS says "deactivate guard" — deactivates both careful and freeze
- DS can deactivate them individually: "deactivate careful" or "deactivate freeze"
- Session ends — both deactivate
