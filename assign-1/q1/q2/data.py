import json

# load data from json file
with open('data.json', 'r') as f:
    data = json.load(f)

# modify data and write it back to another file
with open('written_file.json', 'w') as f:
    json.dump(data, f)

print(data)

