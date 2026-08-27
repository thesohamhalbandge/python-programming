s = "python is very easy and it is oop language"
print(s)
word = s.split(" ") # ['python', 'is', 'very', 'easy', 'and', 'it', 'is', 'oop', 'language']
print(word)

new_word = s.split(" ", 3)
print(new_word) # ['python', 'is', 'very', 'easy and it is oop language']