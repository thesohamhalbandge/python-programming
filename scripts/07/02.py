i = 1

while i <= 10:
    if i == 5:
        break
    print(i, end=" ")
    i += 1

while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i, end=" ")
    i += 1

i = 10
if i == 10:
    pass 
else:
    pass