s = {}
print(type(s)) # <class 'dict'>

s = set()
print(type(s)) # creates an empty set -> <class 'set'>

s = {10, 20, 30, 40, 50, 23.4, 10, True, "sai"}
print(s) # {True, 40, 10, 50, 20, 23.4, 30, 'sai'}

s = {True, 1, False, 0}
print(s) # {False, True}