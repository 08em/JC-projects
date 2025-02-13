fileHandle = open("studentNames.txt", 'w') # 'r' = read ; 'w' = write ; 'a' = append

fileHandle.write("Ian\n")  # \n for the next line
fileHandle.write("Matthew\n")
fileHandle.write("Adrian\n")

fileHandle.close()

# fileHandle = open("studentNames.txt", 'w')
# fileHandle.write("Tiffany\n") #overwrites the previous file

fileHandle = open("studentNames.txt", 'a')
fileHandle.write("Tiffany\n") 

fileHandle.close()

fileHandle = open("studentNames.txt", 'r')

studentNames = [0,0,0,0,0]

for i in range(5):
    textFromFile = fileHandle.readline().rstrip() #strip()/rstrip() removes any blank spaces/lines
    studentNames[i] = textFromFile
fileHandle.close()

for i in range(4):
    print(studentNames[i])

fileHandle = open("Numbers.txt", 'r')

numArr = [0,0,0,0,0,0,0,0]
for i in range(8):
    textFromFile = fileHandle.readline().rstrip() #strip()/rstrip() removes any blank spaces/lines
    numArr[i] = textFromFile

index = 0
Pass = 0
swap = True
while swap == True and index < 7 :
    for index in range(7-Pass):
        swap = False
        if numArr[index] > numArr[index+1] :
            temp = numArr[index]
            numArr[index] = numArr[index+1]
            numArr[index+1] = temp
            swap = True
    Pass = Pass + 1

print(numArr)

fileHandle.close()