import json
dictionary={
    "employee" :{"name" : "Badrinath" ,"age" : 20 ,"city" : "hyderabad"},
    "employees":{"john","binnu","babu"},
    "rank":(1,2,3),
    "father" :"Ram",
    "salary" : 50000,
    "height" : 5.5,
    "employed" : True,
    "married" : False,
    "children":None,
    }
json_object= json.dumps(dictionary,indent = 9)

with open("sample.json","w") as outfile:
    outfile.write(json_object)