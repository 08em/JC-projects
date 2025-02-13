string1 = "shuaib" #python by default does not support character data type, can use both double and single quotes for string
char1 = "o"

# pseudocode
# string1 <- "ppppp"
# char1 <- 'q'

print(len(string1))
print(len(char1)) #in pseudocode, length of a character is always 1

# in python, string is an array of characters ; in pseudocode, a string is a sequence of characters

print(string1[0])

for char in range(len(string1)):
    print(string1[char])

print(string1[0:6])
print(string1[:6])
print(string1[:])
print(string1[-1])