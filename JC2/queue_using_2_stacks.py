stack1 = [None for i in range(5)]
stack2 = [None for i in range(5)]

basePointer1 = 0
topPointer1 = -1 
basePointer2 = 0
topPointer2 = -1 
stackFull = len(stack1) - 1

def enqueue(item):
    if stackFull:
        print("queue is full, cannot add")
