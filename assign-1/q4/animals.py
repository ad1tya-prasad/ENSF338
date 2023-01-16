import json

def add_unique_id(filepath):
    # Load the data from the JSON file
    with open(filepath, 'r') as f:
        data = json.load(f)

    # Add a unique ID field to each record
    for i, record in enumerate(data):
        record['unique_id'] = i

    # Save the data to a new file
    with open('animals_modified.json', 'w') as f:
        json.dump(data, f)

add_unique_id('assign-1/q4/animals.json')
