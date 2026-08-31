s1 = "python is very easy and it is oop language"

s2 = s1.split(" ")
print(s2) # ['python', 'is', 'very', 'easy', 'and', 'it', 'is', 'oop', 'language']
print(type(s2)) # <class 'list'>

s3 = s1.partition(" ")

# help(str.partition)
# partition(self, sep, /) unbound builtins.str method
#     Partition the string into three parts using the given separator.

#     This will search for the separator in the string.  If the separator
#     is found, returns a 3-tuple containing the part before the
#     separator, the separator itself, and the part after it.

#     If the separator is not found, returns a 3-tuple containing
#     the original string and two empty string

print(s3) # ('python', ' ', 'is very easy and it is oop language')
print(type(s3)) # <class 'tuple'>