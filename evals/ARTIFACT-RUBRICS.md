# Artifact Rubrics

Use these rubrics to decide whether an artifact is genuinely fit for downstream use.

## BOOTCAMP-SCOPE.md
- Must name one headline use case and one success metric with a number.
- Must identify real source systems and named data owners.
- Must not confuse dashboard requests with operational decisions.

## ONTOLOGY-VISION.md
- Must model entities, links, and actions from the operating reality.
- Must name what is intentionally deferred.
- Must not collapse the ontology into a UI sitemap.

## ONTOLOGY-ARCHITECTURE.md
- Must define keys, links, actions, and test coverage.
- Must tie objects to backing datasets or call out the gap.
- Must not leave writeback semantics ambiguous.

## PIPELINE-ARCHITECTURE.md
- Must define source-to-output flow and scheduling.
- Must identify quality checks and transform boundaries.
- Must not assume unavailable data access.

## DATA-CONNECTION-STATUS.md
- Must identify status, sync mode, and owner for each critical source.
- Must document any credential, network, or schema blocker.
- Must not include raw secrets.

## PIPELINE-BUILD-STATUS.md
- Must show ontology-ready outputs and quality evidence.
- Must identify the transform or dataset behind each dependency.
- Must not hide partial manual steps.

## WORKSHOP-BUILD-STATUS.md
- Must show the actual operator flow and state of key pages/actions.
- Must separate demo-ready paths from placeholders.
- Must not imply the UI is finished when key actions are blocked.

## AIP-AGENT-STATUS.md
- Must document context scope, tools, and eval results.
- Must show at least one safety-sensitive test path.
- Must not widen agent permissions without explicit rationale.

## OSDK-BUILD-STATUS.md
- Must justify why OSDK is needed.
- Must identify OAuth scope decisions and unresolved gaps.
- Must not drift from the ontology contract.

## SLATE-BUILD-STATUS.md
- Must justify why Slate is needed.
- Must name integration risks and maintenance burden.
- Must not masquerade as the default path when it is exceptional.

## REVIEW-REPORT.md
- Must prioritize findings by severity.
- Must distinguish fix-now issues from strategic questions.
- Must not be a passive summary with no action path.

## SECURITY-AUDIT.md
- Must include severity, exploit path, and remediation.
- Must state a verdict.
- Must not normalize vague or unbounded access.

## QA-REPORT.md
- Must provide explicit readiness evidence and a health score.
- Must include at least one negative or edge-path test.
- Must not call a flow healthy without execution evidence.

## DEPLOYMENT-PLAN.md
- Must state rollout strategy, rollback owner, and preconditions.
- Must reference QA and security outcomes.
- Must not assume production cutover without explicit approval.

## TRAINING-MATERIALS.md
- Must match the actual delivered workflow.
- Must identify support ownership and escalation.
- Must not promise capabilities that are not deployed.

## RETRO-REPORT.md
- Must tie lessons back to the original scope and outcomes.
- Must identify what changes next time.
- Must not sanitize avoidable mistakes.
