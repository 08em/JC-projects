myArr = [0] * 10 # w/o the *10, the array is dynamic. now it assumes the data type is integer & is fixed size of 10
print(myArr)

myNewArr = [0 for i in range(10)]
print(myNewArr)

# to initialise array, can also do :
Arr = [None] * 10
print(Arr)

Array = [None for i in range(10)]
print(Array)

# how to print ; in Alevel can just do print(myArr) its ok
for i in range(len(myArr)):
    print(myArr[i]) 

# how to input into an array
for i in range(len(myArr)):
    myArr[i] = input("Enter a value: ")


for i in range(10) :
    item = input("enter a value: ")
    myArr.append(item) 

