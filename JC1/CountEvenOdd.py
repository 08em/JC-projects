import math

def count():
    num = 0
    even = 0
    odd = 0
    while num != 99:
        num = int(input("enter number: "))
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print(f"there are {even} even numbers and {odd} odd numbers")

count()