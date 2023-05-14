import json

with open("output/arknights_data.json") as arknights_data_json:
    op_data = json.load(arknights_data_json)

for key in op_data["operators"].keys():
    op_data["operators"][key]["icon"] = op_data["operators"][key]["icon"].replace("static/", "")

with open("output/arknights_data.json", "w") as arknights_data_json:
    json.dump(op_data, arknights_data_json, indent=4, sort_keys=True)