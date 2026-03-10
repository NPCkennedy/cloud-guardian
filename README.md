#CLOUD GUARDIAN LITE

An Azure-native governance automation tool.
cloud resources created without proper tags create compliance and audit risk
in regulated organisations.


#What it does:

1. Scans Azure resources for missing required tags
2. Writes a JSON compliance report with timestamp
3. Sends a Teams alert via Azure Logic Apps
4. Uses Azure OpenAI to explain the compliance risk in plain English

Infrastructure deployed with Terraform.
Scanner runs automatically via GitHub Actions CI/CD pipeline.


#REQUIRED TAGS TO ENFORCE

Three tags are checked on every resource:
Owner          - who is responsible for this resource
Environment    - is this dev, staging, or production prevents accidental changes to production resources
CostCenter     - internal billing code for internal cost allocation and audit trails
In scanner.py this is simply:
REQUIRED_TAGS = ['Owner', 'Environment', 'CostCenter']


#TECH STACK
Python 3.11
Azure Function App (Python runtime)
Azure Logic Apps (HTTP trigger to Teams)
Azure OpenAI (gpt-35-turbo) with fallback to OpenAI API if quota unavailable
Terraform
GitHub Actions
Azure DefaultAzureCredential
Packages: azure-identity, azure-mgmt-resource, requests, openai


REPOSITORY STRUCTURE
cloud-guardian/
README.md
requirements.txt
main.tf
variables.tf
.gitignore
.github/workflows/scanner.yml
src/scanner.py       - connects to Azure, lists resources, checks tags
src/ai_advisor.py    - sends violations to Azure OpenAI with fallback
src/notifier.py      - calls Logic Apps webhook for Teams alert
src/report.py        - writes violations.json
tests/test_scanner.py
notes/               - learning notes
DEBUGGING.md         - real bugs encountered, diagnosed, and fixed during the build


BUILD PHASES

PHASE 1: THE SCANNER 
Connect to Azure using DefaultAzureCredential
List resources in cloud-guardian-rg using ResourceManagementClient
Check each resource for Owner, Environment, and CostCenter tags
Write violations.json report with timestamp and summary
Packages: azure-identity azure-mgmt-resource

PHASE 2: ALERTS AND CI/CD
Azure Logic Apps HTTP trigger connected to Teams channel
notifier.py calls Logic Apps webhook when violations found
GitHub Actions pipeline runs scanner on push and daily at chosen time
GitHub Secrets for all credentials - nothing hardcoded

PHASE 3: AI ADVISOR AND TERRAFORM 
Primary: Azure OpenAI gpt-35-turbo called with violation list
Fallback: if Azure OpenAI quota unavailable use OpenAI API directly
Same Python code structure, just different client configuration
import openai then openai.ChatCompletion.create instead of AzureOpenAI
Returns plain English compliance risk explanation
Explanation added to JSON report and Teams message
main.tf creates: resource group, service plan, function app, storage account
terraform init then plan then apply deploys everything


PHASE 1: THE SCANNER

Goal: Python script that authenticates to Azure, lists all resources,
checks for required tags, and produces a JSON compliance report.

Required tags to enforce: Owner and Environment

Core functions in scanner.py:
  check_tags(resource, required_tags) - returns list of missing tags
  scan_resource_group(subscription_id, resource_group_name)
  generate_report(violations) - writes violations.json

Packages: pip install azure-identity azure-mgmt-resource
Test locally: az login then python src/scanner.py

Success criteria:
  Connects to real Azure
  Detects missing tags correctly
  Produces clean JSON report
  Code committed with clear messages
