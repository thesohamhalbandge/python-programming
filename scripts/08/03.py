l = [10, 20, 30, 40, 50]
print(l)

l1 = l # shallow copy
print(l1)

l.append(33)
print(l) # [10, 20, 30, 40, 50, 33]
print(l1) # [10, 20, 30, 40, 50, 33]

print(id(l)) # 1454886271104
print(id(l1)) # 1454886271104

l = [10, 20, 30, 40, 50]
l1 = l.copy() # deep copy

l.append(33)

print(l) # [10, 20, 30, 40, 50, 33]
print(l1) # [10, 20, 30, 40, 50]

print(id(l)) # 2683605771136
print(id(l1)) # 2683605381056