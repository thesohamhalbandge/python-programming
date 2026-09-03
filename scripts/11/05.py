d = {
    "id": 123,
    "name": "manoj",
    "age": 34
}

# d.pop("name")
# print(d) # {'id': 123, 'age': 34}

# d.pop("address") -> KeyError 

value = d.pop("name")
print(value) # manoj
print(d) #  {'id': 123, 'age': 34}

d = {
    "id": 123,
    "name": "manoj",
}

removed_value = d.popitem()
print(removed_value) # ('name', 'manoj')
print(d) # {'id': 123}

