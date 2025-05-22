# 2a)
class Queue :
    def __init__(self):
        self.QueueArray =[0 for i in range(100)]
        HeadPointer = 0 # integer
        TailPointer = 0 # integer

# b)
class Queue1 :
    def __init__(self):
        self.QueueArray = [-1 for _ in range(100)]
        self.HeadPointer = -1
        self.TailPointer = 0

TheQueue = Queue1()

# c)

def Enqueue(AQueue, TheData):
    if AQueue.HeadPointer == -1 :
        AQueue.HeadPointer = 0
        AQueue.QueueArray[AQueue.HeadPointer] = TheData
        AQueue.TailPointer += 1
        return AQueue, 1
    elif AQueue.TailPointer > 99 :
            return AQueue, -1
    else:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.TailPointer += 1
        return AQueue, 1
    
# d) 
def ReturnAllData(TheQueue) :
    temp = ""
    for i in range(TheQueue.HeadPointer, TheQueue.TailPointer):
        temp = temp + str(TheQueue.QueueArray[i]) + " "

    return temp 

# e) i.
for i in range(10):
    valid = False
    while valid == False: 
        num = int(input("enter number that is 0 or greater: "))
        if num >= 0 :
            valid = True

    TheQueue, value = Enqueue(TheQueue, num)
    if value == -1 :
        print("queue is full")
    else:
        print("item was added to queue")

print(ReturnAllData())

# ii. ss

# f)

def Dequeue(AQueue):
    if AQueue.HeadPointer == -1 or AQueue.HeadPointer == 100:
        return AQueue, -1
    else :
        value = AQueue.QueueArray[AQueue.HeadPointer]
        AQueue.HeadPointer += 1
        return AQueue, value
    
# g) i. 
for i in range(2):
    TheQueue, returnVal = Dequeue(TheQueue)
    if returnVal == -1 :
        print("Queue empty")
    else:
        print(returnVal)

# i. ss