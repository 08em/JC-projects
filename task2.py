# task 2 : use a 2d array, total the columns of the elements, total the rows of the elements, find highest of columns n rows

myArr = [[1,17],
         [3, 11],
         [20, 12],
         [5, 9]]

totalCol = 0
totalRow = 0
highestCol = 0
highestRow = 0

for r in range(len(myArr)):
    for c in range(len(myArr[r])):
        totalCol = totalCol + myArr[r][c]

        if myArr[r][c] > highestCol:
            highestCol = myArr[r][c]
        totalRow = totalRow + myArr[r][c]
    
        if totalRow > highestRow:
            highestRow = totalRow
    print("the total of row", r, "is", totalRow)
        

print("the total of the columns is", totalCol)
print("the total of the rows is", totalRow)
print("the highest column is", highestCol)
print("the highest row is", highestRow)




    


        

