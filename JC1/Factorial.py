def fact(num):
    sum = 1
    for index in range(1, num+1):
        sum = sum * index
    return sum

Number = int(input("enter number to find its factorial: "))
tempSum = fact(Number)
print(f"the factorial of {Number} is {tempSum}")
