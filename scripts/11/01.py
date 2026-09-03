d = {}
print(d) # {}
print(type(d)) # <class 'dict'>

d = {1: "sai", 2: "raj", 3: "ram"}
print(d) # {1: 'sai', 2: 'raj', 3: 'ram'}
print(type(d))

d = {1: "sai", 1: "raj", 3: "ram"}
print(d) # {1: 'raj', 3: 'ram'}

# d = {[1, 2, 3]: "sai", 1: "raj", 3: "ram"} -> TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
# print(d)

