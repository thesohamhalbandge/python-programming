A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# union
print(A | B) # {1, 2, 3, 4, 5, 6, 7, 8 }
print(A.union(B)) # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection
print(A & B) # {4, 5}
print(A.intersection(B)) # {4, 5}

# difference
print(A - B) # {1, 2, 3}
print(A.difference(B)) # {1, 2, 3}
print(B.difference(A)) # {8, 6, 7}

# symmetric difference
print(A ^ B) # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B)) # {1, 2, 3, 6, 7, 8}