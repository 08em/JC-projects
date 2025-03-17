# 1a)

StackData = [0 for i in range(10)]
StackPointer = 0
topPointer = -1

# b)

def printStack():
    for i in range(len(StackData)):
        print(StackData[i])

    print("stack pointer is", StackPointer)

# c)
stackFull = len(StackData)

def Push(item):
    global StackPointer, topPointer
    if StackPointer == stackFull :
        return "FALSE"
    else:
        topPointer = topPointer + 1
        StackData[topPointer] = item
        StackPointer = StackPointer + 1
        return "TRUE"
    
# d) i.

i = 1
while i < 12:
    num = int(input("enter an integer: "))
    temp = Push(num)
    if temp == "FALSE":
        print("value was not added to the stack as it is full")
    else:
        print("value was successfully added to the stack")

    i = i + 1

print(StackData)

# ii. is screenshot

# e) i. 

def Pop():
    global StackPointer, topPointer
    if topPointer == -1:
        return -1
    else:
        poppedItem = StackData[topPointer]
        StackData[topPointer] = 0 
        StackPointer = topPointer
        topPointer = topPointer - 1
        return poppedItem
    
# ii. 
Pop()
Pop()
print(StackData)