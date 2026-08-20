s = "" 
print(s)
print(type(s))

s1 = {}
print(s1)
print(type(s1)) # dict 

s2 = set()
print(s2)
print(type(s2))

s3 = {10, 20, 30, 40}
print(s3) # {40, 10, 20, 30} -> unordered
print(type(s3))

s4 = {10, 20, 30, 40, 50, 10}
print(s4) # {50, 20, 40, 10, 30} -> no duplicates
print(type(s4))

s5 = {1, True, 0, False}
print(s5) # {0, 1}

s5.add("new_item")
print(s5) # {0, 1, 'new_item'}

s5.remove(1)
print(s5) # {0, 'new_item'}

fs = frozenset(s5)
print(fs, type(fs))

# fs.add("add_new_item") -> this will throw an error