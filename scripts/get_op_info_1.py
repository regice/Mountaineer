from bs4 import BeautifulSoup
import requests
import json

# NOTE: For operator icon and skins, use a different script!

INTERACTIVE_OPERATOR_LIST_URL = "https://gamepress.gg/arknights/tools/interactive-operator-list#tags=null##cn##stats"

response = requests.get(INTERACTIVE_OPERATOR_LIST_URL)
soup = BeautifulSoup(response.text, "html.parser")
with open("output/arknights_data.json") as arknights_data_json:
    op_data = json.load(arknights_data_json)

with open("output/arknights_branches.json") as arknights_branches_json:
    op_branches = json.load(arknights_branches_json)

# Get td's that contain operator data
op_rows = soup.find_all(name="tr", class_="operators-row")

for op in op_rows:
    op_name = op["data-name"]
    op_rarity = int(op["data-rarity"])
    op_class = op["data-profession"]
    op_branch = op["data-profession-subclass-id"]
    # Make key for operator e.g. "Nearl the Radiant Knight" -> "nearl_the_radiant_knight"
    # Also replace ', (, and ) in operator names
    op_key = op_name.lower().replace(" ", "_").replace("'", "").replace("(", "").replace(")", "")

    # TODO : modify this so that it doesn't wipe other keys such as skin and icon file path every time this script is run
    op_data["operators"][op_key] = {
        "name": op_name,
        "rarity": op_rarity,
        "class": op_class,
        "branch": op_branches[op_branch]
    }

    if op_key not in op_data["operators"].keys():
        pass

with open("output/arknights_data.json", "w") as arknights_data_json:
    json.dump(op_data, arknights_data_json, indent=4, sort_keys=True)