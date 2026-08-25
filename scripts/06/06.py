for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")

for i in range(1, 11):
    if i == 5 or i == 8:
        continue
    print(i, end=" ")

for i in range(1, 101):
    if i in range(20, 71):
        continue 
    print(i, end=" ")