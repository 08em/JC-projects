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
    print(DataArray)

printArray()
