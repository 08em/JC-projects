
# tree = [[-1, i+1, -1] for i in range(10)]
# tree[9][1] = -1

tree = [[1, 9, 2], [3, 7, -1,], [4, 13, 5], [-1,5,-1], [-1, 12, -1], [-1, 15, -1], [-1, 7, -1], [-1, 8, -1], [-1, 9, -1], [-1, -1, -1]]
rootPointer = 0
freePointer = 6

def searchTree(item):
    pointer = rootPointer
    while pointer != -1 and item != tree[pointer][1]:
        if tree[pointer][1] > item:
            pointer = tree[pointer][0]
        if tree[pointer][1] < item:
            pointer = tree[pointer][2]

    return pointer
    
searchEle = int(input("enter search element: "))

if searchTree(searchEle) == -1:
    print("element is not found")
else:
    print("element is found at", searchTree(searchEle))


def insertToTree(item):
    
    if freePointer == -1:
        print("tree is full")
    else:
        newItemPointer = freePointer
        freePointer = tree[newItemPointer][1]
        if rootPointer == -1:
            rootPointer = newItemPointer
            tree[newItemPointer][1] = item
        
        if item > tree[]
