# 2a)
import random
rows, cols = (10, 10)
DataArray = [[0 for i in range(cols)] for j in range(rows)]

for r in range(10):
    for c in range(10):
        DataArray[r][c] = random.randint(1, 100)

# b) i.

arrayLength = 10
for x in range(len(DataArray)-1):
    for y in range(len(DataArray)-2):
        for z in range(len(DataArray)-y-2):
            if DataArray[x][z] > DataArray[x][z+1]:
                tempValue = DataArray[x][z]
                DataArray[x][z] = DataArray[x][z+1]
                DataArray[x][z+1] = tempValue

# ii.
def printArray():
    for r in range(10):
        string = " "
        for c in range(10):
            string = string + " " + str(DataArray[r][c])
        print(string)


printArray()

# iii. take screenshot

# c) i. 

def BinarySearch(SearchArray, Lower, Upper, SearchValue): # RETURNS INTEGER
    if Upper > Lower :
        Mid = (Lower + (Upper)) // 2
        if int(SearchArray[0][Mid]) == SearchValue :
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue :
                return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
            
    return -1
            
# ii. 
searchVal = int(input("enter number to search: "))
print(BinarySearch(DataArray, 0, 9, searchVal))
searchVal = int(input("enter number to search: "))
print(BinarySearch(DataArray, 0, 9, searchVal))