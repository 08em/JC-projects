Arr = [9, 7, 3, 1, 5, 12, 15, 10, 13]
index = 0
Pass = 0
swap = True
while swap == True and index < 9 :
    for index in range(4-Pass):
        swap = False
        if Arr[index] > Arr[index+1] :
            temp = Arr[index]
            Arr[index] = Arr[index+1]
            Arr[index+1] = temp
            swap = True
    Pass = Pass + 1

print(Arr)

Array = [10,13,9,7,6,5,4,3,2,1,24]
lowerBound = 0
upperBound = 10
top = lowerBound
swap = True
# for count in range(lowerBound, upperBound)
while top <= upperBound and swap == True:
    swap = False
    for index in range(lowerBound, upperBound-top):
        if Array[index] > Array[index+1] :
            temp = Array[index]
            Array[index] = Array[index+1]
            Array[index+1] = temp
            swap = True
    top = top + 1
    print(Array)
