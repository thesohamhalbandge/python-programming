t = ()
print(t) 
print(type(t)) 

t = (10)
print(t) # 10
print(type(t)) # <class 'int'>

t = (10, )
print(t) # (10,)
print(type(t)) # <class 'tuple'>

t = "mohan", 10, 20.3, True, None, 10, 20, 10, 20
print(t)
print(type(t)) # <class 'tuple'>

# t[1] = 55 -> this will throw an error 

# deleting entire the tuple
del t 
# print(t) -> this will throw NameError
