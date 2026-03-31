# pstack — Palantir Deployment Strategist AI Team

## Skill routing

When you see these patterns, INVOKE the skill via the Skill tool:

```
- User describes a new customer engagement → invoke /bootcamp
- User asks about strategic ontology modeling → invoke /ontology-vision
- User asks to lock ontology architecture → invoke /ontology-architect
- User asks about data pipeline design → invoke /pipeline-plan
- User asks to configure data connections → invoke /data-connector
- User asks to build pipeline transforms → invoke /pipeline-builder
- User asks to build Workshop apps → invoke /workshop-builder
- User asks to configure AIP agents → invoke /aip-architect
- User asks to build OSDK applications → invoke /osdk-developer
- User asks to build Slate apps → invoke /slate-builder
- User asks to review Foundry work → invoke /foundry-reviewer
- User asks about security audit → invoke /foundry-security
- User asks to test or run QA → invoke /foundry-qa
- User asks to deploy via Apollo → invoke /apollo-deployer
- User asks about training materials → invoke /training-writer
- User asks for retrospective → invoke /deployment-retro
- User asks for safety mode → invoke /careful or /guard
- User asks to restrict scope → invoke /freeze
```

## Project structure

```
pstack/
├── skills/              # Agent SKILL.md files
│   ├── bootcamp/        # AIP Bootcamp discovery
│   ├── ontology-vision/ # Strategic ontology design
│   ├── ontology-architect/ # Ontology architecture lock
│   ├── pipeline-plan/   # Pipeline architecture design
│   ├── data-connector/  # Data Connection configuration
│   ├── pipeline-builder/# Transform development
│   ├── workshop-builder/# Workshop app development
│   ├── aip-architect/   # AIP agent design
│   ├── osdk-developer/  # OSDK app development
│   ├── slate-builder/   # Slate app development
│   ├── foundry-reviewer/# Structural audit
│   ├── foundry-security/# Security audit
│   ├── foundry-qa/      # End-to-end testing
│   ├── apollo-deployer/ # Apollo deployment
│   ├── training-writer/ # Training materials
│   └── deployment-retro/# Retrospective
├── templates/           # Artifact templates
├── docs/                # Supporting documentation
├── ETHOS.md             # Design principles
├── ARCHITECTURE.md      # System architecture
└── README.md            # Project overview
```

## Conventions

- Every skill produces a named artifact (e.g., `BOOTCAMP-SCOPE.md`, `ONTOLOGY-ARCHITECTURE.md`).
- Artifacts chain: each skill reads upstream docs and produces downstream docs.
- Use AskUserQuestion for all DS decisions. Never act on strategic choices without confirmation.
- The Ontology is both the product being built AND the coordination mechanism.
- All Palantir tool configurations should reference official documentation.
- When in doubt about Palantir API behavior, state uncertainty — don't guess.
