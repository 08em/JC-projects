# linked list can be implemented using either 2 1d arrays or 1 2d array
# start pointer holds address of first node in linked list
# heap pointer to first available location 
# dataArray = [None for i in range(6)] 
# pointerArray = [None for i in range(6)]
# for index in range(len(pointerArray)): 
#    pointerArray[index] = index + 1
# pointerArray[len(pointerArray)-1] = -1

dataArray = [5, 6, 9, 3, None, None, None]
pointerArray = [-1, 0, 1, 2, 5, 6, -1]

startPointer = 3
heapPointer = 4
maxSize = len(dataArray) - 1

print(pointerArray)

# i = startPointer
# while i != -1:
#    print(dataArray[i])
#    i = pointerArray[i]

def addToList(item):
    global startPointer, heapPointer
    if heapPointer != -1:
        tempPointer = startPointer
        startPointer = heapPointer
        dataArray[startPointer] = item
        heapPointer = pointerArray[heapPointer] 
        pointerArray[startPointer] = tempPointer
    else : 
        print("linked list is full, cannot add")

addToList(2)
addToList(7)
addToList(1)
addToList(3)

print(dataArray)
print(pointerArray)
print("sp is", startPointer)
print("hp is", heapPointer)


def deleteFromList(item) :
    global startPointer, heapPointer
    if startPointer == -1 : # if list is empty, cannot remove anyth
        print("list is empty, nothing to remove")
    
    else:
        itemPointer = startPointer
        while item != dataArray[itemPointer] and itemPointer != -1:
            oldPointer = itemPointer
            itemPointer = pointerArray[itemPointer]
        
        if itemPointer == -1:
            print("item not found")

        else:
            dataArray[itemPointer] = None
            pointerArray[oldPointer] = pointerArray[itemPointer]
            pointerArray[itemPointer] = heapPointer
            heapPointer = itemPointer


deleteFromList(9)
print(dataArray)
print(pointerArray)
print("sp is", startPointer)
print("hp is", heapPointer)

deleteFromList(1)
print(dataArray)
print(pointerArray)
print("sp is", startPointer)
print("hp is", heapPointer)