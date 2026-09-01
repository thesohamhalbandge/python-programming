numbers_list = [1, 7, 2, 9, 3, 0]

list_length = len(numbers_list)
print(f"The length of the list is: {list_length}\n")

print("Elements greater than the list length:")

for element in numbers_list:
    if element > list_length:
        print(element)