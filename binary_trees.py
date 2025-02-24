
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
    global freePointer, rootPointer
    if freePointer == -1:
        print("tree is full")
    else:
        newItemPointer = freePointer
        freePointer = tree[newItemPointer][1]

        if rootPointer == -1:
            rootPointer = newItemPointer
            tree[newItemPointer][1] = item
        else: 
            tempPointer = rootPointer
            if item > tree[tempPointer][1] :
                while tree[tempPointer][2] != -1:
                    tempPointer = tree[tempPointer][2]
                if item > tree[tempPointer][1] :
                    tree[tempPointer][2] = newItemPointer
                else: 
                    tree[tempPointer][0] = newItemPointer

            else: 
                while tree[tempPointer][0] != -1:
                    tempPointer = tree[tempPointer][0] 
                tree[tempPointer][0] = newItemPointer
                if item > tree[tempPointer][1] :
                    tree[tempPointer][2] = newItemPointer
                else: 
                    tree[tempPointer][0] = newItemPointer

            tree[newItemPointer][1] = item

print(tree)
insertToTree(3)
print(tree)
insertToTree(20)
print(tree)
insertToTree(16)
print(tree)
insertToTree(2)
print(tree)
insertToTree(8)
print(tree)