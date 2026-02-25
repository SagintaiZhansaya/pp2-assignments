import json

with open("sample-data.json") as file:
    data = json.load(file)

for item in data["imdata"][:3]:
    attributes = item["l1PhysIf"]["attributes"]
    
    print(attributes["dn"],
          attributes["descr"],
          attributes["speed"],
          attributes["mtu"])