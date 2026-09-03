d = {
    "id": 1,
    "name": "raj",
    "address": "hyderabad"
}

print(d["id"]) # 1
# print(d["age"]) KeyError -> 'age'

print(d.get("id")) # 1
print(d.get("age")) # None -> this will not throw an error even if key doesn't exist
print(d.get("age", "there is no age key")) # there is no age key

# changing value
print(d) # {'id': 1, 'name': 'raj', 'address': 'hyderabad'}
d["address"] = "sr nagar"
print(d) # {'id': 1, 'name': 'raj', 'address': 'sr nagar'}

d["age"] = 33
print(d) # {'id': 1, 'name': 'raj', 'address': 'sr nagar', 'age': 33}

# deleting keys
del d["name"]
print(d) # {'id': 1, 'address': 'sr nagar', 'age': 33}

# deleting dict
del d 
# print(d) NameError: name 'd' is not defined. Did you mean: 'id'?