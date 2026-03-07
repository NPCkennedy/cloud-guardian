#Check if a resource has all required tags.
#Returns a list of tag names that are missing.
#Returns an empty list if all tags are present.

def check_tags(resource, required_tags):
	
	missing = []
	for tag in required_tags:
		if tag not in resource["tags"]:
			missing.append(tag)
		return missing

#Scan all resources and print a compliance report.
def generate_report(resources, required_tags):
	total_violations = 0
	print("Cloud Guardian - Tag Compliance Report")
	print("======================================")
	for resource in resources:
		missing = check_tags(resource, required_tags)
		if missing:
			print(f"VIOLATION: {resource['name']} is missing tags: {missing}")
			total_violations += 1
	print("======================================")
	print(f"Scanned: {len(resources)} resources | Violations: {total_violations}")

if __name__ == "__main__":
	resources = [
		{"name": "vm-prod-01",  "type": "VirtualMachine", "tags": {"Owner": "Alice"}},
		{"name": "storage-dev", "type": "StorageAccount", "tags": {}},
		{"name": "func-app-01", "type": "FunctionApp",   "tags": {"Owner": "Bob"}},
		{"name": "db-staging",  "type": "SQLDatabase",   "tags": {}},
		{"name": "vnet-main",   "type": "VirtualNetwork","tags": {"Owner": "Charlie"}},
		]
required_tags = ["Owner", "Environment"]
generate_report(resources, required_tags)