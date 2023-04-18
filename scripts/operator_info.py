from bs4 import BeautifulSoup
import requests
import json

INTERACTIVE_OPERATOR_LIST_URL = "https://gamepress.gg/arknights/tools/interactive-operator-list#tags=null##cn##stats"

response = requests.get(INTERACTIVE_OPERATOR_LIST_URL)
soup = BeautifulSoup(response.text, "html.parser")
with open("output/arknights_data.json") as arknights_data_json:
    op_data = json.load(arknights_data_json)

# Get td's that contain operator data
op_rows = soup.find_all(name="tr", class_="operators-row")

for op in op_rows:
    op_name = op["data-name"]
    op_rarity = int(op["data-rarity"])
    op_class = op["data-profession"]
    # Make key for operator e.g. "Nearl the Radiant Knight" -> "nearl_the_radiant_knight"
    op_key = op_name.lower().replace(" ", "_")

    op_data["operators"][op_key] = {
        "name": op_name,
        "rarity": op_rarity,
        "class": op_class,
        "branch": "",
        "icon": "",
        "skins": []
    }

with open("output/arknights_data.json", "w") as arknights_data_json:
    json.dump(op_data, arknights_data_json, indent=4, sort_keys=True)