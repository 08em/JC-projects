def addTwoNumbers() :
    num1 = 6
    num2 = 5
    sum = num1 + num2
    return sum

tempSum = addTwoNumbers()
print("the sum is", tempSum)

def addTwoNumbers(num1, num2) :
    sum = num1 + num2
    return sum

number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))
tempSum = addTwoNumbers()
print("the sum is", tempSum)