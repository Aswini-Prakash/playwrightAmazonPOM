import json

def searchiteamjson_load():
    with open('testdata\\searchitems.json', 'r') as file:
        data = json.load(file)
    return data