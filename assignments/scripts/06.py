# write a program to print lower case and upper case characters separately and also print lower case count and upper case count separately

string = "Hello World ABC xyz"
lower_case = ""
upper_case = ""

for i in string:
    if i.isupper():
        upper_case += i 
    elif i.islower():
        lower_case += i

print("Upper case characters: [", upper_case, "]; Length of upper case characters:", len(upper_case))
print("Lower case characters: [", lower_case, "]; Length of lower case characters:", len(lower_case))