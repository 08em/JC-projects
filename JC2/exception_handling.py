num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

try:
    print("quotient is: ", num1 / num2)
except ZeroDivisionError:                   # if this error/exception occurs:
    print("cannot divide by zero")          # then this happens

try:
    file = open("shuaib.txt", 'r')
except FileNotFoundError:
    print("file trying to be opened does not exist")
    
array = [None for i in range(10)]

try: 
    print(array[20])
except IndexError:
    print("index is out of range")