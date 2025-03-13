# task 1 : total all of the elements and get the highest n lowest values

myArr = [2, 4, 11, 1, 8, 6, 7]

top = len(myArr) - 1
swap = True
total = 0

while swap == True:
    swap = False
    for i in range(top):
        total = total + myArr[i]
        if myArr[i] > myArr[i+1]:
            temp = myArr[i]
            myArr[i] = myArr[i+1]
            myArr[i+1] = temp
            swap = True
    top = top - 1

lowest = myArr[0]
highest = myArr[len(myArr)-1]

print(myArr)
print("total of the elements is", total, ", lowest value is", lowest, "highest value is", highest)