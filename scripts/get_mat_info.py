import json

with open("output/arknights_data.json") as arknights_data_json:
    data = json.load(arknights_data_json)

print("This is the script for inputting new materials. Enter '.stop' to terminate the program.")

continue_loop = True
while continue_loop is not False:
    print("CAUTION: Please make sure to enter '.stop' in order to save work.")
    new_mat = input("New material's name?: ")

    if new_mat == ".stop":
        continue_loop = False
    else:
        img_path = input("Image path of the new material?: ")
        item_grade = int(input("Tier of the material?: "))
        mat_key = new_mat.lower().replace(" ", "_")

        # Add new entry
        data["items"][mat_key] = {
            "img_path": img_path,
            "name": new_mat,
            "tier": item_grade
        }

# for key in data["items"]:
#     data["items"][key]["tier"] = 0

with open("output/arknights_data.json", "w") as arknights_data_json:
    json.dump(data, arknights_data_json, indent=4, sort_keys=True)