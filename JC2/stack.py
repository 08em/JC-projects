# need 2 pointers, top and base
# base always points to 0, top points to topmost item and is -1 if stack is empty
# MUST check if stack is empty or full before popping/pushing an item onto the stack

stackArray = [None for i in range(10)]

stackFull = len(stackArray)
basePointer = 0
topPointer = -1


def push(item):
    global topPointer
    if topPointer == stackFull:
        print("stack is full, cannot push item onto stack")
    else:
        topPointer = topPointer + 1
        stackArray[topPointer] = item

def pop():
    global topPointer
    if topPointer == -1:
        print("stack is empty, cannot push any item")
        return -1
    else:
        value = stackArray[topPointer]
        topPointer = topPointer - 1
        return value

push(3)
push(6)
push(10)
push(4)
push(8)
push(7)
pop()
pop()
pop()

print(stackArray)
print(topPointer)
