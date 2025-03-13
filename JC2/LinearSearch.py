array = [1,2,3,4,5]
search = int(input("enter value to be found: "))
found = False

for i in range(len(array)):
    if search == array[i]:
        found = True


if found == True:
    print("value was found in array")
else:
    print("value was not found in array")