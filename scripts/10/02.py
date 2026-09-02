s = {1, True, 0, False, 10, 20, 30}
print(s) # {0, 1, 20, 10, 30}
print(type(s))

s.add(33) # {0, 1, 33, 20, 10, 30}
print(s)

s.update([10, "raj", 50])
print(s) # {0, 1, 33, 50, 20, 'raj', 10, 30}

s.discard(10)
print(s) # {0, 1, 33, 50, 20, 'raj', 30}
s.discard(100) # 
print(s) # {0, 1, 33, 50, 20, 'raj', 30}

# it works same as discard but if element is not there then remove will throw an error 
# s.remove(100) -> KeyError: 100

s.clear()
print(s) # set() and not {}
print(type(s)) # <class 'set'>

del s 
# print(s) ->  NameError