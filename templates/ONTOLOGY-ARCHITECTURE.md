# Ontology Architecture Template

**Usage:** Produced by `/ontology-architect`. Consumed by all build agents.

---

# Ontology Architecture: [Customer Name]

**Date:** [YYYY-MM-DD]
**Upstream:** ONTOLOGY-VISION.md, BOOTCAMP-SCOPE.md

## Object Types

### [Object Type Name]

```
Display Name: [Human-readable]
Plural: [Plural form]
Description: [What this represents]
Primary Key: [property] (type)
Title Property: [display property]
Icon: [Foundry icon name]
Backing Dataset: [/path/to/dataset]
```

| Property | Display Name | Type | Backing Column | Required | Editable | Searchable | Description |
|----------|-------------|------|----------------|----------|----------|------------|-------------|
| | | | | | | | |

## Link Types

| Name | From | To | Cardinality | FK Column | Display (fwd) | Display (rev) |
|------|------|-----|-------------|-----------|---------------|---------------|
| | | | | | | |

## Action Types

### [Action Name]

```
Display Name: [Human-readable]
Description: [What it does]
Object Type: [Target]
```

| Parameter | Type | Required | Validation |
|-----------|------|----------|------------|
| | | | |

**Logic:** [What changes when executed]
**Audit:** [Yes/No]

## Functions

| Name | Language | Input | Output | Purpose |
|------|----------|-------|--------|---------|
| | | | | |

## Interfaces

| Name | Properties | Applied To |
|------|-----------|------------|
| | | |

## Edge Cases

| Edge Case | Object Type | Resolution |
|-----------|-------------|------------|
| | | |

## Test Plan

### Object Type Tests
- [ ] All types populated (row count > 0)
- [ ] Primary keys unique
- [ ] Required properties non-null

### Link Tests
- [ ] All links resolve (<5% dangling)
- [ ] Cardinality matches spec

### Action Tests
- [ ] Valid params → success
- [ ] Invalid params → clear error

### Function Tests
- [ ] Known inputs → expected outputs
- [ ] Null handling → graceful
