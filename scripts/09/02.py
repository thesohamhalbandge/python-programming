t = (10, 20, 10, 10, 20, 10, 30, 10, 10)
print(t.count(10)) # 6
print(t.count(100)) # 0
print(t.index(20)) # 1

print(10 in t)  # True
print(100 in t) # False
print("sai" not in t) # True 

print(len(t)) # 9
print(max(t)) # 30
print(min(t)) # 10
print(sum(t)) # 130