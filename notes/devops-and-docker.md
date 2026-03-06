What is DevOps?

Culture + practices that bridge Development (writing code) and Operations (running it reliably).
Goal: Faster, more reliable software delivery through collaboration, automation, and feedback loops.
Not just tools — it's about people, process, and culture.

Core Principles (CALMS framework – remember this!)

Culture: Collaboration between dev, ops, security (no silos).
Automation: Automate builds, tests, deployments, infrastructure.
Lean: Eliminate waste (manual steps, waiting).
Measurement: Track metrics (deployment frequency, lead time, failure rate).
Sharing: Feedback loops, blameless post-mortems.

Why it matters?

AI-driven ops, multi-cloud, edge computing demand speed + security.
Regulated orgs need audit trails, ownership → DevOps enables automated compliance.

Key Practices

Continuous Integration (CI): Merge code often + auto-build/test.
Continuous Delivery/Deployment (CD): Auto-deploy to prod safely.
Infrastructure as Code (IaC).
Monitoring + observability.
Shift-left security (DevSecOps).

takeaway
DevOps = automate everything repeatable so teams ship faster without breaking things.

-----------------------------------------------------------------------------------------------------------

What is Docker?

Tool for creating, shipping, and running applications in containers.
Container = lightweight, portable package with code + dependencies (libs, runtime, config).
Solves "it works on my machine" problem.

Core Concepts

Image — Read-only blueprint/template (like a class or snapshot). Built from Dockerfile. Stored in registries (Docker Hub, Azure Container Registry).
Container — Running instance of an image (like an object). Isolated but shares host kernel → fast & efficient (vs VM).
Dockerfile — Text file with instructions to build an image (FROM base image, COPY code, RUN commands, CMD to start app).
Docker Hub / Registry — Public/private place to store & share images.
Volumes — Persistent storage for data (containers are ephemeral by default). Mount host folder or use named volumes.
Networks — How containers talk (bridge = default, host, none, custom).
Docker Compose — Tool (YAML file) to run multi-container apps (e.g., app + database).
Lifecycle — docker build → docker run → docker stop/rm → docker logs/ps.

Docker vs Virtual Machine

VM: Full OS + hypervisor → heavy, slow boot.
Container: Shared kernel + isolated processes → lightweight, seconds to start.

Why DevOps engineers use Docker

Consistent environments (dev, test, prod).
Easy scaling & orchestration (leads to Kubernetes).
CI/CD: Build once, run anywhere.

takeaway
Containers package apps + deps so they run the same everywhere — foundation for modern cloud-native apps.