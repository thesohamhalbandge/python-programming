s = "python is very easy"
s1 = s.split(" ")
print(type(s1))
print(s1)

s1.sort()
print(s1)

s1.sort(reverse=True)
print(s1)

s2 = " ".join(s1)
print(s2)