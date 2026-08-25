a = 10 
b = 20
print(a is b) # False 
print(a is not b) # True

print(id(a))
print(id(b))

a = 10
b = 10.0
print(a is b) # False
print(a is not b) # True 