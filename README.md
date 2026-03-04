# cloud-guardian

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

  sahsvdiuyvaeuf
  renote commit
