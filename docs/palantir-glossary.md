# Palantir Platform Glossary

Reference for all pstack agents. Every agent should use these terms consistently.

---

## Core Concepts

**Ontology** — Palantir's semantic layer that maps real-world entities to digital
representations. The ontology sits between raw data and applications, providing a
shared language for humans and machines to interact with enterprise data. Everything
in Palantir connects through the ontology.

**Object Type** — A category of real-world entity modeled in the ontology. Examples:
Patient, Order, Asset, Employee. Defined by a name, properties, and a backing dataset.
Analogous to a class in object-oriented programming or an entity in ER modeling.

**Object** — A specific instance of an object type. "Patient John Smith" is an object
of the Patient object type. Objects have property values and links to other objects.

**Property** — An attribute of an object type. Examples: firstName, status, acuityScore.
Each property has a type (String, Integer, Timestamp, etc.) and is backed by a column
in the backing dataset.

**Link Type** — A defined relationship between two object types. Examples: Patient
"assigned to" Provider, Order "contains" LineItem. Links have cardinality (1:1, 1:many,
many:many) and direction.

**Action Type** — A defined operation that modifies ontology objects. Examples: "Assign
Patient to Bed," "Approve Order," "Escalate Alert." Actions have parameters, validation
rules, and writeback targets.

**Function** — A computed value or operation defined on the ontology. Written in
TypeScript or Python. Examples: calculateAcuityScore(), getOpenOrderCount(). Functions
can query objects, compute derived values, and return results.

**Interface** — A set of shared properties that multiple object types implement.
Examples: Auditable (createdBy, createdAt), Locatable (latitude, longitude). Enables
polymorphic queries across object types.

**Backing Dataset** — The Foundry dataset that provides data for an object type.
Each row in the backing dataset becomes an object. Each column maps to a property.

**Primary Key** — The property that uniquely identifies each object within an object
type. Must be unique and non-null in the backing dataset.

---

## Products

**Foundry** — Palantir's data integration and operational platform. The core product
for commercial and government customers. Contains all data management, ontology,
application, and AI capabilities.

**Gotham** — Palantir's platform for defense and intelligence community customers.
Focused on intelligence analysis, mission planning, and operational decision-making.
Predates Foundry and has some unique capabilities for classified environments.

**AIP (Artificial Intelligence Platform)** — Palantir's AI layer that sits on top
of the ontology. Enables LLM-powered agents, logic functions, and automated workflows
grounded in enterprise data. The key differentiator: AI operates on the ontology,
not raw data, so it inherits security, governance, and semantic context.

**Apollo** — Palantir's continuous delivery and deployment platform. Manages software
deployment across cloud, hybrid, on-premise, and air-gapped environments. Uses a
hub-and-spoke architecture with release channels (canary, stable, release).

**OSDK (Ontology SDK)** — Developer toolkit for building custom applications on top
of the ontology. Generates type-safe client libraries in TypeScript, Python, and Java
from the ontology definition. Enables building React apps, backend services, and
integrations that read/write ontology data.

---

## Tools and Applications

**Pipeline Builder** — No-code/low-code tool for building data transformation
pipelines. Supports joins, filters, aggregations, type casting, and LLM-powered
transforms through a visual interface. Preferred for simple-to-moderate transforms.

**Code Repositories** — Git-based development environment for writing data
transforms in Python, SQL, or Java. Preferred for complex transforms, custom logic,
ML model inference, and advanced Spark operations. Integrated with Foundry's build
system.

**Code Workspaces** — VS Code-based development environment within Foundry.
Supports collaborative editing, terminal access, and direct integration with
Foundry datasets and the ontology.

**Data Connection** — Tool for connecting external data sources to Foundry. Supports
200+ connector types including JDBC databases, REST APIs, cloud storage (S3, Azure
Blob, GCS), SFTP, streaming (Kafka, Kinesis), and enterprise systems (SAP, Salesforce,
ServiceNow, Workday). Can deploy agents for on-premise/air-gapped sources.

**Workshop** — No-code application builder for creating operational applications.
Provides a widget library (Object Tables, Maps, Charts, Forms, Buttons, AIP Agent),
an event system for inter-widget communication, and variable-based state management.
The primary tool for building user-facing applications.

**Slate** — Legacy application builder with full HTML/CSS/JavaScript flexibility.
Supports custom widgets, Handlebars templates, Leaflet maps, and external API
integration. More flexible than Workshop but higher maintenance burden.

**Contour** — Analytical tool for exploring and analyzing Foundry datasets. Supports
pivot tables, charts, filters, and derived columns. Good for ad-hoc analysis.

**Quiver** — Advanced analytics and dashboarding tool. Supports complex
visualizations, cross-dataset analysis, and embeddable dashboard components.
Often embedded within Workshop applications for executive-level metrics.

**Object Explorer** — Tool for browsing and inspecting individual ontology objects.
Shows properties, links, actions, and timeline. Useful for development and debugging.

**Vertex** — Graph visualization tool for exploring entity relationships. Renders
link topology as interactive node-graph diagrams. Used for investigation and
network analysis.

**Notepad** — Collaborative document tool within Foundry. Supports rich text,
ontology object references, and embedded visualizations. Used for analysis reports,
meeting notes, and knowledge management.

---

## AIP Components

**AIP Assist** — Chat interface available throughout Foundry applications. Allows
users to ask natural language questions about their data. The simplest AIP interaction
model.

**AIP Agent Studio** — Tool for designing and configuring AI agents. Agents have
context sources (ontology objects, document sets), tools (actions, queries, functions),
system prompts, and model selection. Agents can be embedded in Workshop or accessed
standalone.

**AIP Logic** — Visual canvas for composing deterministic LLM workflows. Uses blocks
(Use LLM, Apply Action, Execute Function, Conditional, Loop) to build multi-step AI
pipelines. More deterministic than free-form agent interactions.

**AIP Automate** — Workflow automation engine that triggers agent or Logic function
execution based on events (object changes, schedules, action completions, webhooks).
Enables autonomous AI operations within defined guardrails.

**AIP Evals** — Evaluation framework for testing AIP agents and Logic functions.
Supports test case definition, expected behavior specification, multi-model comparison,
and automated quality scoring.

---

## Data Concepts

**Dataset** — A table of data stored in Foundry. Datasets have schemas (column names
and types), transactions (historical versions), and branches (development isolation).
Datasets are the foundational data unit.

**Data Lineage** — The complete trace of how a dataset was created, including all
upstream datasets, transforms, and data sources. Foundry automatically tracks lineage
for governance and debugging.

**Build** — The execution of a transform pipeline that produces output datasets from
input datasets. Builds can be scheduled, triggered by upstream builds, or run manually.

**Branch** — An isolated version of a dataset or pipeline for development. Similar
to Git branches. Allows testing transforms without affecting production data.

**Transaction** — A specific version of a dataset. Foundry maintains full transaction
history, enabling time-travel queries and audit trails.

**Incremental Pipeline** — A pipeline that processes only new or modified data since
the last build, rather than reprocessing the entire dataset. Reduces compute cost and
build time for large datasets.

---

## Security and Governance

**Marking** — A security label applied to data that controls access. Markings
implement attribute-based access control. Examples: "PII," "CONFIDENTIAL," "ITAR."
Users must have the corresponding marking grant to access marked data.

**Organization** — A top-level access control boundary in Foundry. Users belong to
organizations, and resources are owned by organizations.

**Group** — A collection of users within an organization. Groups are granted
permissions on resources. Examples: "Data Engineers," "Analysts," "Executives."

**Role** — A set of capabilities that can be assigned to users or groups on specific
resources. Standard roles: Viewer, Editor, Owner.

**Purpose-Based Access Control** — Access control that restricts data usage to
specific approved purposes, beyond simple read/write permissions.

---

## Deployment Concepts

**Forward Deployed Engineer (FDE)** — Historical Palantir role. An engineer embedded
at the customer site who builds and maintains Palantir deployments. Predecessors to
today's deployment strategists.

**Deployment Strategist (DS)** — The modern version of the FDE. Combines technical
platform expertise with customer-facing strategic thinking. Responsible for
translating customer operational needs into Palantir platform solutions.

**AIP Bootcamp** — Palantir's intensive engagement format. Typically 3-5 days of
focused work with customer stakeholders to go from problem identification to
working prototype. Designed to demonstrate value quickly.

**Center of Excellence (CoE)** — A customer's internal team trained to maintain
and extend their Palantir deployment independently. The goal of every engagement
is to build CoE capability.

**Hub-and-Spoke (Apollo)** — Apollo's deployment architecture where a central hub
manages software distribution to spoke environments. Spokes can be cloud instances,
on-premise servers, edge devices, or air-gapped networks.

**Release Channel** — Apollo's mechanism for staged software rollout. New versions
progress through channels (canary → stable → release) with configurable bake times
and rollback triggers.
