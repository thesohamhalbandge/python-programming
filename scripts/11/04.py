d = {
    "id": 123,
    "name": "manoj",
    "address": "hyd"
}

print(d.items()) # dict_items([('id', 123), ('name', 'manoj'), ('address', 'hyd')])

print(d.keys()) # dict_keys(['id', 'name', 'address'])

print(d.values()) # dict_values([123, 'manoj', 'hyd'])

for k, v in d.items():
    print(k, "=", v)

print(123 in d) # False
print("id" in d) # True

print(len(d)) # 3
d = {}
print(len(d)) # 0


