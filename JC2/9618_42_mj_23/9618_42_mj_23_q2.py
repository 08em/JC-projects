# 2a)
class SaleData :
    def __init__(self, saleID, quantity):
        self.saleID = saleID # string
        self.quantity = quantity # integer

# b)
CircularQueue = [SaleData("", -1)for i in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0

# c) 
def Enqueue(record):
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = record
        if tail == 4:
            tail = 0
        else:
            tail += 1
            NumberOfItems += 1
        return 1

# d)
def Dequeue():
    record = SaleData("", -1)
    if NumberOfItems == 0 :
        return record
    else:
        record = CircularQueue[Head]
        if Head == 4:
            Head = 0
        else:
            Head = Head + 1
        
        NumberOfItems = NumberOfItems - 1

        return record
    
# e)  
def EnterRecord(ID, Qty):
    record = SaleData(ID, Qty)
    result = Enqueue(record)
    if result == -1 :
        print("Full")
    else: 
        print("Stored")

# f) i.
EnterRecord("ADF", 10)
EnterRecord("OOP", 1)
EnterRecord("BXW", 5) 
EnterRecord("XXZ", 22)
EnterRecord("HQR", 6)
EnterRecord("LLP", 3) 
Dequeue()
EnterRecord("LLP", 3)
print(CircularQueue)

# ii. screenshot