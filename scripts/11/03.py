d = {
    "id": 123,
    "name": "manoj",
    "address": "hyd"
}

d1 = d
d["name"] = "mohan"

print(d) # {'id': 123, 'name': 'mohan', 'address': 'hyd'}
print(d1)# {'id': 123, 'name': 'mohan', 'address': 'hyd'}

print(id(d)) # 2088999284480
print(id(d1)) # 2088999284480

d1 = d.copy()

print(d1) # {'id': 123, 'name': 'mohan', 'address': 'hyd'}
print(d) # {'id': 123, 'name': 'mohan', 'address': 'hyd'}

d1["name"] = "kratos"
print(d1) # {'id': 123, 'name': 'kratos', 'address': 'hyd'}
print(d) # {'id': 123, 'name': 'mohan', 'address': 'hyd'}