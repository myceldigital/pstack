# Bootcamp Scope: Acme Supply Chain Control Tower

**Date:** 2026-03-31  
**DS:** Maya Chen  
**Industry:** Discrete manufacturing  
**Engagement type:** Expansion from dashboard POC to operational pilot

## Executive Summary

Acme Components wants to move from retrospective supply-chain reporting to live operational decisions for expedite management and supply risk. The five-day bootcamp is scoped to prove that planners can see the right at-risk orders, understand the causal bottleneck, and initiate a governed expedite or escalation path before customer promise dates are breached.

## Use Cases

### Use Case 1: Expedite At-Risk Orders ★★★ HEADLINER

**Operational decision:** Should the planner pay expedite cost, re-sequence production, or accept customer-date risk for an order line?  
**Current workflow:** Regional planners merge SAP order extracts, Blue Yonder shipment feeds, and supplier emails in Excel, then escalate by phone.  
**Workflow gap:** The team cannot reliably identify which delayed component is actually on the critical path, so expediting is both late and expensive.  
**Success metric:** Reduce expedite decision latency from 4.5 hours to under 45 minutes for top-priority orders and cut unnecessary expedites by 15%.  
**Data readiness:** 8/10  
**Estimated build time:** 4 bootcamp days  
**Demo audience:** COO, VP Supply Chain, regional planning manager, plant scheduling lead

#### Preliminary Ontology Sketch
- Object types: `Shipment`, `OrderLine`, `InventoryPosition`, `SupplierCommit`, `RiskCase`, `ExpediteRequest`
- Key relationships: order line backed by component inventory, order line linked to supplier commit and shipment, risk case linked to affected order line
- Critical properties: customer promise date, latest supplier ETA, stock coverage hours, expedite cost estimate, risk severity
- Action types: create expedite request, assign owner, mark supplier escalation, acknowledge resolution

### Use Case 2: Supplier Delay Triage ★★ QUICK WIN

**Operational decision:** Which supplier delay requires buyer escalation today versus passive monitoring?  
**Current workflow:** Buyers rely on supplier scorecards and inbox triage.  
**Workflow gap:** Delay alerts are disconnected from customer impact and available substitution inventory.  
**Success metric:** Reduce buyer investigation time per material shortage from 35 minutes to 10 minutes.  
**Data readiness:** 7/10  
**Estimated build time:** 2 bootcamp days  
**Demo audience:** Procurement director, supplier performance manager

#### Preliminary Ontology Sketch
- Object types: `Supplier`, `SupplierCommit`, `Material`, `Plant`, `RiskCase`
- Key relationships: supplier commit to supplier and material, material to plant demand, risk case to supplier commit
- Critical properties: commit date variance, open quantity, supplier risk tier, shortage severity
- Action types: escalate supplier, request alternate source review, accept delay

### Deferred Use Cases

- Supplier quality non-conformance workflow: deferred because the source system of record is managed by a separate quality program and was not available during bootcamp week.
- Automated transport re-booking: deferred because carrier writeback and financial approval flows need legal and controls review.

## Data Inventory

| Source System | Data | Format | Refresh | Owner | Readiness | Bootcamp Day |
|---------------|------|--------|---------|-------|-----------|--------------|
| SAP ECC | sales orders, purchase orders, delivery schedules, plants, materials | JDBC | 15 min extract | ERP product owner | 9/10 | Day 1 |
| Blue Yonder TMS | shipment milestones, carrier status, lane ETAs | REST API | 15 min | Logistics systems manager | 8/10 | Day 1 |
| SPS Commerce EDI 214 | in-transit events, ASN updates | S3 drops | near-hourly | B2B integration lead | 7/10 | Day 2 |
| Supplier Portal | commit dates, partial-ship confirmations, shortages | CSV export | daily | Procurement ops lead | 6/10 | Day 2 |
| Kinaxis planning export | inventory coverage, constrained demand, substitution candidates | CSV | 4-hourly | Planning excellence lead | 7/10 | Day 3 |

## Stakeholder Map

| Role | Name | Cares about | Skeptical of | Demo target |
|------|------|-------------|--------------|-------------|
| COO sponsor | Elena Rossi | service-level performance, expedite spend, planner throughput | another reporting tool with no action path | final day decision demo |
| VP Supply Chain | Marcus Bell | cross-plant prioritization and exception management | low data trust in supplier updates | day 3 checkpoint |
| Regional planning manager | Dana Patel | faster triage and less spreadsheet work | noisy alerts with no business context | daily walkthrough |
| Procurement director | Omar Schmitt | supplier accountability and shortage visibility | false positives that trigger unnecessary escalations | supplier triage slice |
| IT integration lead | Sarah Kim | secure connectivity and operational supportability | custom connectors with no owner | architecture sign-off |

## Bootcamp Schedule (Proposed)

| Day | Morning | Afternoon | Demo/Check-in |
|-----|---------|-----------|---------------|
| 1 | sponsor framing, use-case lock, SAP + TMS data review | ontology sketch, source-to-decision mapping | sponsor checkpoint |
| 2 | EDI and supplier-portal onboarding, shortage logic review | pipeline design, risk scoring draft | planner review |
| 3 | ontology architecture lock, Workshop page flow | first end-to-end data slice, risk-case prototype | VP supply chain walkthrough |
| 4 | action design, QA path definition, security review prep | build hardening, agent eval design | technical gatekeeper review |
| 5 | final demo rehearsal, rollout discussion | executive demo, next-phase recommendation | steering committee |

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| EDI events arrive late or out of order for ocean and LTL shipments | High | High | show freshness and confidence explicitly; do not allow auto-close on stale data |
| Supplier portal data contains manual overrides with inconsistent part identifiers | Medium | High | normalize supplier part map in clean layer and flag unresolved crosswalks |
| Customer wants carrier re-booking in pilot scope | Medium | Medium | keep actions approval-gated and frame writeback as phase 2 |
| Plant teams disagree on expedite thresholds | Medium | Medium | encode thresholds by business unit and keep them editable only for admins |
| Global rollout pressure pulls in EU plants before North America is stable | Medium | High | recommend phased deployment with one canary region and explicit exit criteria |

## Next Steps

1. [ ] DS to confirm North America pilot region and top-20 customer list with COO staff.
2. [ ] Customer to provide service account and schema sample for SAP ECC and Blue Yonder TMS.
3. [ ] Run `/ontology-vision` on the locked expedite and supplier-delay scope.
4. [ ] Run `/pipeline-plan` on SAP, TMS, EDI, supplier portal, and planning-export sources.
