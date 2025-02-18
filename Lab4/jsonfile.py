import json

file_path = r"C:\Users\user\Downloads\sample-data.json"
with open(file_path, 'r') as file:
    data = json.load(file)

output = []
output.append("Interface Status")
output.append("=" * 100)
output.append("DN                                                 Description           Speed    MTU  ")
output.append("-" * 100)

for item in data["imdata"][:3]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"].strip() if attributes["descr"].strip() else ""
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    output.append(f"{dn:50} {descr:20} {speed:7} {mtu:6}")

print("\n".join(output))
