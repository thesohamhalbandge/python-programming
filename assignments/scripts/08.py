string = input("Enter a string: ")

list_string = string.split(" ")

for i in list_string:
    print(i[::-1], end=" ")