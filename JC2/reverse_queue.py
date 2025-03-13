# reverse a queue using stack
queueArray = [2, 6, 1, 3, 4]
frontPointer = 0
rearPointer = 4
maxSize = len(queueArray)
lenOfQueue = 5

poppedItem = 0
dequeuedItem = 0

def enqueue(item):
    global lenOfQueue, rearPointer
    if lenOfQueue == maxSize :
        print("queue is full")
    else:
        if rearPointer == maxSize - 1:
            rearPointer = 0

        rearPointer = rearPointer + 1
        queueArray[rearPointer] = item
        lenOfQueue = lenOfQueue + 1


def dequeue():
    global lenOfQueue, frontPointer, dequeuedItem
    if lenOfQueue == 0:
        print("queue is empty")
    else:
        dequeuedItem = queueArray[frontPointer]
        lenOfQueue = lenOfQueue - 1

        if frontPointer == maxSize - 1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1



stackArray = [None for i in range(5)]

stackFull = len(stackArray) - 1
basePointer = 0
topPointer = -1
lenOfStack = 0

def push(item):
    global topPointer, lenOfStack
    if topPointer == stackFull:
        print("stack is full, cannot push item onto stack")
    else:
        topPointer = topPointer + 1
        stackArray[topPointer] = item
        lenOfStack = lenOfStack + 1

def pop():
    global topPointer, poppedItem
    if topPointer == -1:
        print("stack is empty, cannot push any item")
    else:
        poppedItem = stackArray[topPointer]
        stackArray[topPointer] = None
        topPointer = topPointer - 1

print(queueArray)
print(stackArray)

while lenOfQueue != 0 :
    dequeue()
    push(dequeuedItem)

while lenOfStack != 0 :
    pop()
    enqueue(poppedItem)
    
print(queueArray)
print(stackArray)