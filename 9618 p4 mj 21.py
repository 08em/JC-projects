arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

found = False
item = int(input("enter data item to be found: "))

def linearSearch(item):
    global found
    for i in range(len(arrayData)):
        if item == arrayData[i]:
            found = True
        else:
            found = False

    print(found)

