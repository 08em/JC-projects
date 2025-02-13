def printMyName(): # def used to define procedure or function
    print("my name is Khan")
    print("i work at BBS")

printMyName()

def sayHello(name):
    print(f"hello {name}")


sayHello("Shuaib")


def addTwoNumbers():
    sum = num1 + num2
    print(f"the sum of {num1} and {num2} is {sum}")

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))


addTwoNumbers()


def demo():
    global number1 # not recommended to do this, better to define in main program
    global number2
    global sum1
    number1 = 6
    number2 = 8
    sum1 = number1 + number2
    print(f"sum of {number1} and {number2} is {sum1}")


demo()
print(f"sum of {number1} and {number2} is {sum1}")


