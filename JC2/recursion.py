# a function which calls itself is a recursive function
# every recursive function must have : a recursive case (a statement calling itself), and a terminal/terminating/end/base case (statement that stops the recursion)
# any problem that can be solved using iteration can be solved using recursion
# advantages of recursion : code looks more elegant, code can be implemented with less statements, reduces complexity of the code
# disadvantages : can crash the program if base case is not defined properly/never met, slower than iteration 

# def recursion():
#     recursion()

# recursion() 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sumArray(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sumArray(array[1:])
    
print(sumArray(arr))

