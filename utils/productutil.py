
import json


def json_load(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["product"]
