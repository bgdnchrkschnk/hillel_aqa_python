import json

# ---------------------------------- .dumps() - from python dict to json string

person_dict: dict = {
    "name": "Volodymyr",
    "age": 48,
    "is_president": True,
    "nationality": ["Ukraine", "Israel"]
}


json_str: str = json.dumps(person_dict, indent=4)

# ----------------------------------- .dump() - write json in file

with open("person_dict.json", "w") as json_file:
    json.dump(person_dict, json_file, indent=4)
    print("Json file successfully created!")


# ----------------------------------- .load() - convert json string to python dict

with open("person_dict.json", "r") as json_file:
    data = json.load(json_file)

# ----------------------------------- .loads() - convert json string to python dict

json_string = """{
    "name": "Volodymyr",
    "age": 48,
    "is_president": true,
    "nationality": [
        "Ukraine",
        "Israel"
    ]
}"""

json_converted_to_dict: dict = json.loads(json_string)
print(type(json_converted_to_dict), json_converted_to_dict)