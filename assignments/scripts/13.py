# write a program to print the second highest value from the list 

l = [10, 20, 4, 45, 353, 2, 74, 99]
l = sorted(list(set(l)))
print(l[-2]) # 30