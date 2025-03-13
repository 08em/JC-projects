# condition to use binary search on array - array MUST be sorted

myArr = [5, 7, 8, 9, 13, 15, 17, 20, 22]
low = 0 # lowest index
high = len(myArr) - 1 # highest index
mid = (low+high) // 2 #find middle index ; // gives the integer division
search = int(input("input element to be found: "))
found = False


while found == False :
    mid = (low+high) // 2
    if search == myArr[mid]:
        found = True

    if search > myArr[mid] :
        low = mid + 1
    else:
        high = mid - 1

    if low == high :
        break

if found == True:
    print("element found")
else:
    print("element not found")

        

