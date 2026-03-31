# Ontology Architecture: Northstar Healthcare Patient Flow

## Object Types

- Core object with unique identifier and status
- Resource object representing available capacity
- Risk object representing operational friction

## Links

- Core object -> resource
- Core object -> risk

## Actions

- Escalate issue
- Reassign work
- Confirm resolution

## Test Plan

- Primary keys unique
- Links resolve
- Actions validate required fields
