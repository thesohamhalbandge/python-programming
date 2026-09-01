# creating list from user input values

n = int(input("Enter the number of elements you want in a list: "))

l = []
for i in range(n):
    element = input("Enter the element you want in a list: ")
    l.append(element)

print(l)