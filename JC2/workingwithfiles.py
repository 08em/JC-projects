# OPENFILE "Numbers.txt" FOR READ/WRITE/APPEND
# READLINE "Numbers.txt", text (this is reading file one line at a time n storing it in text)

file = open("Numbers.txt", 'r') # r for read, w for write, a for append
# text = file.read() # read = reads entire file n stores everyth 
# print(text)


# text3 = file.readline()  # reads one line n stores it 
# print(text) # when printing, also prints extra space bc enter key is considered a character

myArr = [0 for i in range(10)]
file = open("Numbers.txt", 'r')
for i in range(10):
    text = file.readline()
    myArr[i] = int(text.strip())


text2 = file.readlines() # stores every line in an array. NOT ALLOWED FOR ALEVEL
print(text2)

total = 0
for x in range(10):
    total = total + int(text2[x].strip())

name = "   shuaib   "
print(name.strip()) # removes all white space
print(name.lstrip()) # removes all white spaces on the left side
print(name.rstrip()) # removes all white spaces on the right side
