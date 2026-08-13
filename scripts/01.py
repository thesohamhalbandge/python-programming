print("hello")
print("world")

# This is my first python comment

# To see keywords list
import keyword
print(keyword.kwlist)

# if = 10 -> this is invalid as if is keyword

age = 30
print(age)
print(type(age)) # to see the datatype of variable
print(id(age)) # to get memory address of variable age

a = b = c = 10
# print(a, b, c)
# print(a, b, c, sep="-")
# print(a, b, c, sep="\n")

a1, b1, c1 = 10, 20, 30
print(a1, end=" ")
print(b1, end=" ")
print(c1)