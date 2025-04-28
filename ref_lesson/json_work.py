import json

# ------------------------------------- .dumps() from python dict to json string
data: dict = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"]
}


json_string = json.dumps(data, indent=4)

print(json_string)


# -------------------------------------- .dump() from python dict write in json file


# Python dict
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"]
}

# Записуємо у файл `output.json` у форматі JSON
with open("json_file.json", "w") as f:
    json.dump(data, f, indent=4)

# ------------------------------------- .load() from json file to python dict

with open("json_file.json", "r") as f:
    data = json.load(f)


print(data) # - Python dict

# --------------------------- .loads() from json string to python dict

json_string = '{"name": "Alice", "age": 30, "is_student": false, "courses": ["Math", "Science"]}'

data = json.loads(json_string)

print(data) # Python dict