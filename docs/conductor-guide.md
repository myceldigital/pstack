# Conductor Guide — How to Orchestrate pstack

## The Conductor Model

You are the conductor of a 16-agent AI team. Each agent is a deep expert in one
part of the Palantir stack. Your job is to:

1. **Set direction** — decide what to build, for whom, in what order
2. **Make strategic decisions** — when agents surface questions, make the call
3. **Manage parallelism** — run 5-10 agents simultaneously on different tasks
4. **Validate with customer** — you own the customer relationship, agents don't
5. **Accept or reject work** — review agent outputs before they go to production

## Daily Bootcamp Workflow

### Day 1: Discover + Data

```
Morning:
  Session 1: /bootcamp — Run discovery with customer SMEs
  Session 2: /pipeline-plan — Design data architecture based on emerging scope

Afternoon:
  Session 3: /data-connector — Start connecting to data sources
  Session 4: /ontology-vision — Begin strategic ontology design

End of day:
  ✓ BOOTCAMP-SCOPE.md complete
  ✓ Data connections initiated
  ✓ Ontology vision drafted
```

### Day 2: Architecture + Build Start

```
Morning:
  Session 1: /ontology-architect — Lock ontology specification
  Session 2: /data-connector — Complete remaining connections
  Session 3: /pipeline-builder — Start transform development

Afternoon:
  Session 4: /pipeline-builder — Continue transforms
  Session 5: /workshop-builder — Start application layout

End of day:
  ✓ ONTOLOGY-ARCHITECTURE.md complete
  ✓ All data connections active
  ✓ Layer 1-2 transforms built
  ✓ Workshop app skeleton created
```

### Day 3: Build + Demo v1

```
Morning:
  Session 1: /pipeline-builder — Complete output datasets
  Session 2: /workshop-builder — Wire events, connect actions
  Session 3: /aip-architect — Configure agents

Afternoon:
  Session 4: /foundry-reviewer — Quick audit of all work
  Demo: Show working v1 to operational lead

End of day:
  ✓ Working Workshop app with real data
  ✓ AIP agent responding to queries
  ✓ Review findings addressed
```

### Day 4: Quick Win + Polish

```
Morning:
  Session 1: /bootcamp — Scope quick win use case (if not done)
  Session 2: /workshop-builder — Build quick win app
  Session 3: /aip-architect — Add second agent or refine first

Afternoon:
  Session 4: /foundry-security — Security audit
  Session 5: /foundry-qa — Run eval suites
  Demo: Show quick win to stakeholders

End of day:
  ✓ Quick win app delivered
  ✓ Security audit clean
  ✓ QA health score ≥85%
```

### Day 5: Deploy + Train + Handoff

```
Morning:
  Session 1: /apollo-deployer — Production deployment
  Session 2: /training-writer — Generate all documentation

Afternoon:
  Session 3: /training-writer — Run training sessions
  Session 4: /deployment-retro — Capture lessons learned
  Final demo: All stakeholders

End of day:
  ✓ Production deployment live
  ✓ Training delivered
  ✓ Documentation complete
  ✓ Retro documented
```

## Parallel Session Management

### Rules for parallelism:

1. **Never run two agents that modify the same artifact simultaneously.**
   Two `/pipeline-builder` sessions working on the same pipeline = conflicts.

2. **Architecture before build.** Don't start `/workshop-builder` until
   `/ontology-architect` has produced `ONTOLOGY-ARCHITECTURE.md`.

3. **Build before review.** Don't start `/foundry-reviewer` until build
   agents have completed their work.

4. **Review before deploy.** Don't start `/apollo-deployer` until review
   and QA are complete.

5. **Independent use cases CAN parallelize.** If Use Case 1 and Use Case 2
   have different data sources and different object types, their build
   agents can run simultaneously.

### Session naming convention:

```
Session 1: [Agent] — [Use Case] — [Specific Task]
Example: /pipeline-builder — Patient Flow — ED-to-Ward transform
```

## Decision Framework

When an agent surfaces a decision via AskUserQuestion:

1. **Read the context** — understand what the agent found
2. **Check the recommendation** — the agent's preferred option
3. **Apply your judgment** — customer relationship, political dynamics,
   timeline constraints, budget, strategic considerations
4. **Decide and move on** — don't agonize. The agent can iterate.

### When to override the agent:

- You know something about the customer the agent doesn't
- The recommended approach won't survive a stakeholder review
- The timeline doesn't support the recommended level of completeness
- The customer has explicitly requested a different approach

### When to trust the agent:

- Technical domain decisions (Spark optimization, property types, widget config)
- Best practice recommendations (Pipeline Builder vs. Code Repositories)
- Security findings (the agent knows the threat model)
- Quality issues (the agent found a real bug)
