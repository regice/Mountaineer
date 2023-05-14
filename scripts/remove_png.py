import json

with open("output/arknights_data.json") as arknights_data_json:
    op_data = json.load(arknights_data_json)

for key, value in op_data["operators"].items():
    new_path = value["icon"].replace(".png", "")

    op_data["operators"][key]["icon"] = new_path

with open("output/arknights_data.json", "w") as arknights_data_json:
    json.dump(op_data, arknights_data_json, indent=4, sort_keys=True)