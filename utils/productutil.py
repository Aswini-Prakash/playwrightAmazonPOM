import json

def read_product():
    with open("testdata/products.json", "r") as file:
        data = json.load(file)

    return data["product"][0]