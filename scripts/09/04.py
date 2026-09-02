a = 10
b = 20
c = 30 

# tuple packing
t = a, b, c 
print(t) # (10, 20, 30)
print(type(t)) # <class 'tuple'>

# tuple unpacking
t = (10, 20, 30)
a, b, c = t 
print("a =", a) # 10
print("b =", b) # 20
print("c =", c) # 30