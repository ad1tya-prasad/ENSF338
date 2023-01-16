import json

# load data from json file
with open('assign-1/q2/data.json', 'r') as f:
    data = json.load(f)

# reverse the data
data.reverse()

# and write it back to another file
with open('assign-1/q2/reversed_data.json', 'w') as f:
    json.dump(data, f)


