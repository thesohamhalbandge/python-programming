l = [10, 20, 30, 40, 10, 20, "sai", 20.4, True]
print(l)
print(type(l))

print(l[3]) # 40
print(l[-3]) # sai

l = [10, 20, [30, 40, "sai"], 20.4, True]
print(l)
print(type(l))
print(l[2][2]) # sai

l = [10, 20, 30, 40]
l[1] = 33
print(l) # [10, 33, 30, 40]

l = [10, 20, 30, 40]
l.insert(1, 33)
print(l) # [10, 33, 20, 30, 40]

l = [10, 20, 30, 40]
print(l)
l.append(33)
print(l) # [10, 20, 30, 40, 33]
l.extend(["sai", True, 4.5])
print(l) # [10, 20, 30, 40, 33, 'sai', True, 4.5]

l = [10, 20, 30, 40, 50]
print(l) # [10, 20, 30, 40, 50]
l.remove(40)
print(l) # [10, 20, 30, 50]

l = [10, 20, 30, 40, 50]
l.pop(2) # will remove 30 i.e. 2nd index
print(l) # [10, 20, 40, 50]

l = [10, 20, 30, 40, 50]
l.clear() 
print(l) # []

# del l 
# print(l) -> this will give an error