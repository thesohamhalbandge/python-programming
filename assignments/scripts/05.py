# write a program to print even index and odd index position characters from given string by using 
# - slice
# - for loop
# - while loop

# using slice
string = "python is very easy and object oriented programming language"
print("Even index characters:", string[::2])
print("Odd index characters:", string[1::2])

# for loop
index_count = 0
even_string = ""
odd_string = ""
for i in string:
    if index_count % 2 == 0:
        even_string += i 
    else:
        odd_string += i
    index_count += 1
 
print("Even character strings:", even_string)
print("Odd character strings:", odd_string)

# while loop
index_count = 0
even_string = ""
odd_string = ""
while index_count < len(string):
    if index_count % 2 == 0:
            even_string += string[index_count] 
    else:
        odd_string += string[index_count]
    index_count += 1

print("Even character strings:", even_string)
print("Odd character strings:", odd_string)