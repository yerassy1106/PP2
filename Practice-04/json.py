# json.py
import json

#Read JSON file
with open("sample-data.json", "r") as file:
    data = json.load(file)

#  Print totalCount
print("Total Count:", data["totalCount"])

#  Print all interface IDs
print("\nAll interface IDs:")
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    print(attributes["id"])

#  Count how many interfaces are enabled
enabled_count = 0

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    if attributes["switchingSt"] == "enabled":
        enabled_count += 1

print("\nEnabled interfaces:", enabled_count)

#  Create new filtered list (only enabled interfaces)
enabled_interfaces = []

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    if attributes["switchingSt"] == "enabled":
        enabled_interfaces.append(attributes)

#  Save filtered data to new file
with open("enabled_interfaces.json", "w") as file:
    json.dump(enabled_interfaces, file, indent=4)

print("\nFiltered data saved to enabled_interfaces.json")