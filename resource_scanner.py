#List of fake Azure resources - some have the Owner tag, some do not
resources = [
{"name": "vm-prod-01",    "type": "VirtualMachine", "tags": {"Owner": "Alice"}},
{"name": "storage-dev",   "type": "StorageAccount", "tags": {}},
{"name": "func-app-01",   "type": "FunctionApp",   "tags": {"Owner": "Bob"}},
{"name": "db-staging",    "type": "SQLDatabase",   "tags": {}},
{"name": "vnet-main",     "type": "VirtualNetwork","tags": {"Owner": "Charlie"}},
]

#Check each resource for the Owner tag and report violations
print("Cloud Guardian - Tag Compliance Report")
print("--------------------------------------")
violations = 0
for resource in resources:
	if "Owner" not in resource["tags"]:
		print(f"VIOLATION: {resource['name']} ({resource['type']}) is missing the Owner tag")
		violations += 1
print(f"--------------------------------------")
print(f"Total violations found: {violations}")