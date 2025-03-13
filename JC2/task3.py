#  a 2d integer array has 'row' rows and 'col' columns. write pseudocode and program code to:
# 1. input a searching value, output the row and column number where the element is present or an appropriate message if the element is not present
# 2. input a searching value and the row number to searching for and output the column number where the element is present or appropriate message if the element is not present
# 3. sort each row of the 2d array using bubble sort and then input a searching value & the row number to searching for & output the column number where the element is present 
# or appropriate message if the element is not present using binary searching

#1. 
arr = [[1, 23, 12],
       [3, 2, 4],
       [5, 10, 13],
       [9, 12, 15]]

found = False
search = int(input("enter search value: "))

for r in range(len(arr)):
    for c in range(len(arr[r])):
        if search == arr[r][c] :
            found = True
            row = r
            col = c

if found == True :
    print("search element was found in row", row, "column", col)
else: 
    print("search element was not found")

# 2. 
array = [[2, 14, 11],
         [4, 6, 8],
         [17, 11, 1],
         [3, 19, 33]]

found2 = False
searchVal = int(input("enter value to be found: "))
rowVal = int(input("enter row to find search value in: "))

for c in range(len(array[c])):
    if searchVal == array[rowVal][c]:
        found2 = True
        column = c

if found == True :
    print("element was found in column", column)
else:
    print("element was not found in row", rowVal)

# 3.

array1 = [ [9, 1, 2, 3],
         [34, 12, 10, 5],
         [15, 6, 10, 31],
         [8, 24, 16, 4]]

top = len(array) - 1
swap = True
total = 0

while swap == True:
    swap = False
    for i in range(top):
        total = total + array1[i]
        if array1[i] > array1[i+1]:
            temp = array1[i]
            array1[i] = array1[i+1]
            array1[i+1] = temp
            swap = True
    top = top - 1

mid = 0
low = 0
high = len(array) - 1
found3 = False

searching = int(input("enter value to be found: "))
rowFind = int(input("enter row to find search value in: "))

while found3 == False:
    mid = (low + high) // 2
    if searching == array1[rowFind][mid]:
        found = True
        colFind = mid

    if searching > array1[rowFind][mid]:
        low = mid + 1
    else:
        high = mid - 1

    if low == high :
        break

if found == True:
    print("element found in column", colFind)
else:
    print("element not found in given row")



    