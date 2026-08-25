# first n numbers sum

num = int(input("Enter a number:"))
sum = 0

for i in range(1, num + 1):
    sum += i

print("The sum:", sum)