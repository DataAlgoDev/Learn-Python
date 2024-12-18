import json

with open('Content Handling/sample4.json', 'r') as file:
    data = json.load(file)

i = 0
while i < len(data['people']):
    first_name = data['people'][i]['firstName']
    if first_name == "Ajay":
        data['people'].pop()
    else:
        i += 1

individual_data = {
       "firstName": "Ajay",
       "lastName": "Narayanan",
       "gender": "male",
       "age": 27,
       "number": "8592996418"
       }

data['people'].append(individual_data)

with open('Content Handling/sample4.json', 'w+') as file:
    json.dump(data, file, indent=4)
    file.seek(0)
    data = json.load(file)
    for i in range(len(data['people'])):
        print(data['people'][i]['firstName'])


