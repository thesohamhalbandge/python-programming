l1 = ["sai", "ganesh", "kiran"]
l2 = ["raj", "manoj"]
print(l1 + l2) # ['sai', 'ganesh', 'kiran', 'raj', 'manoj']

print(l1 * 3) # ['sai', 'ganesh', 'kiran', 'sai', 'ganesh', 'kiran', 'sai', 'ganesh', 'kiran']

l = [-9, 1, 0, 4, 7, 6, 5, 2, 3, 10]
print(l)
l.sort()
print(l) # [-9, 0, 1, 2, 3, 4, 5, 6, 7, 10]

l.sort(reverse=True)
print(l) # [10, 7, 6, 5, 4, 3, 2, 1, 0, -9]