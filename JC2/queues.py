queue = [None for i in range(5)]
frontPointer = 0
rearPointer = -1
maxSize = len(queue)
lenOfQueue = 0

def enqueue(item):
    global lenOfQueue, rearPointer, frontPointer
    if lenOfQueue == maxSize :
        print("queue is full")
    else:
        if rearPointer == maxSize - 1:
            rearPointer = 0
        else: 
            rearPointer = rearPointer + 1
            queue[rearPointer] = item
            lenOfQueue = lenOfQueue + 1


def dequeue():
    global lenOfQueue, frontPointer
    if lenOfQueue == 0:
        print("queue is empty")
    else:
        item = queue[frontPointer]
        lenOfQueue = lenOfQueue - 1

        if frontPointer == maxSize - 1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
            
        return item

enqueue(5)
print(queue)

enqueue(15)
print(queue)

enqueue(33)
print(queue)

enqueue(12)
print(queue)

enqueue(9)
print(queue)

enqueue(1)
print(queue)

dequeue()
print(queue)
dequeue()
print(queue)
dequeue()
print(queue)


enqueue(3)
print(queue)

enqueue(7)
print(queue)

dequeue()
print(queue)
dequeue()
print(queue)
dequeue()
print(queue)

