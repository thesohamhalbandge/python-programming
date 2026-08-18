l = [10, 20, 30, 40, 50]
print(l)
print(type(l))

l[1] = 99
print(l)

t = ()
print(t)
print(type(t))

t1 = (10)
print(t1)
print(type(t1)) # <class 'int'>

t2 = (10, )
print(t2)
print(type(t2))

# ---------------------------------

import sys 

l = [10, 20, 30]
t = (10, 20, 30)

print(sys.getsizeof(l)) # 88
print(sys.getsizeof(t)) # 72 -> tuple is memory efficient