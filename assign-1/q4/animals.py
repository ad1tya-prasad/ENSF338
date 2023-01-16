import json

def average_above_5(filepath):
    # Load the data from the JSON file
    with open(filepath, 'r') as f:
        data = json.load(f)

    # initialize sum and count
    sum = 0
    count = 0
    # iterate over the data
    for record in data:
        # if the value is above 5
        if record['weight'] > 5:
            sum += record['weight']
            count += 1
    # if there are records above 5
    if count > 0:
        avg = sum/count
        print(avg)
    else:
        print("There are no records above 5")

average_above_5('assign-1/q4/animals.json')

