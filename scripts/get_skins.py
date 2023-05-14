from bs4 import BeautifulSoup
import requests
import json

SKIN_LIST_URL = "https://gamepress.gg/arknights/database/skin-list"

response = requests.get(SKIN_LIST_URL)
soup = BeautifulSoup(response.text, "html.parser")
# with open("output/arknights_data.json") as arknights_data_json:
#     op_data = json.load(arknights_data_json)

with open("output/arknights_skins.json") as arknights_skins_json:
    skin_data = json.load(arknights_skins_json)

skin_names = soup.find_all(name="td", class_="views-field-title")
skin_ops = soup.find_all(name="td", class_="views-field-field-skin-operator")

# print(len(skin_names))
# print(len(skin_ops))

for x in range(len(skin_names)):
    skin_name = skin_names[x].contents[-2].string
    op_name = skin_ops[x].contents[0].string
    op_key = op_name.lower().replace(" ", "_").replace("'", "").replace("(", "").replace(")", "")
    skin_key = skin_name.lower().replace(" ", "_")

    # print(f"Skin Name: {skin_name} | "
    #       f"Operator: {op_name}")

    # Make entry for operator if not in dictionary
    if op_key not in skin_data["skins"].keys():
        skin_data["skins"][op_key] = {}

    # Add skin to operator entry if not already in there
    if skin_key not in skin_data["skins"][op_key].keys():
        skin_data["skins"][op_key][skin_key] = ""

with open("output/arknights_skins.json", "w") as arknights_skins_json:
    json.dump(skin_data, arknights_skins_json, indent=4, sort_keys=True)
