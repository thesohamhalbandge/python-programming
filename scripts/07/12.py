s = "hyderabad is awesome"
print(len(s)) # 20

s = "python is very easy and it is oop language"
print(s.find("is")) # will find the first occurence -> 7
print(s.find("x")) # -1 [if substring not available find will give -1 and there will be no error]

print(s.index("is")) # will find the first occurence -> 7
# print(s.index("x")) -> this will throw ValueError [if substring not available index will give error]

print(s.rindex("is")) # 27

# ASCII
for i in "python":
    print(ord(i), end=" ") # 112 121 116 104 111 110

print()
print(max("python")) # y
print(min("python")) # h
print(ord("n")) # 110