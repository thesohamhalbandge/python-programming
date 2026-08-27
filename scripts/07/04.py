s = "hyderabad"

# indexing
print(s[2]) # d
print(s[-2]) # a 
print(s[7]) # a
# print(s[12]) -> index error

# Slicing
print(s[3:7]) # erab
print(s[7:3]) # ""
print(s[:6]) # hydera
print(s[4:]) # rabad
print(s[-3:-7]) # ""
print(s[-7:-3]) # dera
print(s[0:9]) # hyderabad
print(s[:9:1]) # start end step
print(s[:9:2]) # hdrbd
print(s[::])  # hyderabad
print(s[::-1]) # string reverse