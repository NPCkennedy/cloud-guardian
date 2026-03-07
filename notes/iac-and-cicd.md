What is Terraform?

Open-source Infrastructure as Code (IaC) tool from HashiCorp.
Declare what infrastructure you want (in .tf files) → Terraform creates/updates/destroys it automatically.

Why IaC > clicking in portal

Repeatable, version-controlled, auditable.
Collaboration via Git.
No drift (reality matches code).
Faster, fewer errors, easier rollbacks.

Core Concepts

Provider — Plugin for a service (e.g., azurerm for Azure, aws for AWS).
Resource — Thing you create (e.g., azurerm_resource_group, azurerm_virtual_machine).
Data sources — Read existing info (e.g., data "azurerm_subscription").
Variables — Input params (variables.tf) for reuse/flexibility.
Outputs — Values Terraform returns (e.g., IP address).
State — terraform.tfstate file tracks real-world resources (critical – back it up!).
Modules — Reusable code blocks (like functions) – e.g., module for VNet.
Lifecycle — init → plan (dry-run) → apply (create) → destroy.

Workflow

Write .tf files.
terraform init (download providers).
terraform plan (preview changes).
terraform apply (make changes).
Commit to Git.

takeaway
Terraform turns infrastructure into code → version it, review changes, automate deployments safely.

--------------------------------------------------------------------------------------------------------------------------

What is CI/CD?

CI (Continuous Integration): Developers merge code frequently → auto build + test.
CD (Continuous Delivery/Deployment): Auto-deploy tested code to staging/prod (manual approval for Delivery, fully auto for Deployment).

Why it solves problems

Catches bugs early.
Reduces integration hell.
Faster feedback.
Reliable releases.

GitHub Actions Basics (your tool in bootcamp/capstone)

YAML workflows in .github/workflows/ folder.
Events trigger runs (push, pull_request, schedule).
Jobs — groups of steps (can run parallel/sequential).
Steps — individual actions (run script, checkout code, use marketplace action).
Runners — VMs (GitHub-hosted or self-hosted).
Secrets — Store keys/tokens securely (GitHub Settings → Secrets).
Artifacts — Save build outputs (e.g., JSON report) for download.

Typical Pipeline Stages

Checkout code.
Build/test/lint.
Scan security/vulns.
Deploy to Azure (e.g., via az cli or Terraform).
Notify (Teams/slack).

takeaway
CI/CD = automate build → test → deploy so changes reach production quickly & safely. GitHub Actions makes it easy inside your repo.


