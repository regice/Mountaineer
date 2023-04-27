from bs4 import BeautifulSoup
import requests
import json

# Updates output/arknights_branches.json with Operator Branches and their respective id on GamePress

INTERACTIVE_OPERATOR_LIST_URL = "https://gamepress.gg/arknights/tools/interactive-operator-list#tags=null##cn##stats"

response = requests.get(INTERACTIVE_OPERATOR_LIST_URL)
soup = BeautifulSoup(response.text, "html.parser")

branch_cells = soup.find_all(name="div", class_="subprofession-filter-inner")

branch_dict = {}

for cell in branch_cells:
    branch_name = cell["data-url-id"]
    branch_id = (''.join(i for i in cell["onclick"] if i.isdigit()))

    separator_index = branch_name.find("-/-")
    if separator_index != -1:
        branch_name = branch_name[(separator_index+3):]

    branch_dict[branch_id] = branch_name

with open("output/arknights_branches.json", "w") as f:
    json.dump(branch_dict, f, indent=4, sort_keys=True)