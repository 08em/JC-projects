arr =[2, 9, 3, 5, 1, 6]



for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while key < arr[j] and j>=0 :
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
        j = j-1

print(arr)


