# Number1 = 300 # Number1 is a variable of type integer
# Number2 = 598 # Number2 is a variable of type integer

# Sum = Number1 + Number2

# print(Sum)


Number1 = int(input("please input first number:")) # Number1 is a variable of type integer
Number2 = int(input("please input second number:")) # Number2 is a variable of type integer

Sum = Number1 + Number2
print("The sum is", Sum)
print("the sum of", Number1, "and", Number2, "is", Sum) #also works for pseudocode
print(f"The sum of {Number1} and {Number2} is {Sum}") #alternative way to write, both methods work, only works for python

Sum = Number1 + Number2
Diff = Number1 - Number2
Prod = Number1 * Number2
Quot = Number1 / Number2
Rem = Number1 % Number2 #works same as MOD
IntQuot = Number1 // Number2 #works same as DIV

print(f"The difference of {Number1} and {Number2} is {Diff}")
print(f"The product of {Number1} and {Number2} is {Prod}")
print(f"The quotient of {Number1} and {Number2} is {Quot}")
print(f"The remainder of {Number1} and {Number2} is {Rem}")
print(f"The integer quotient of {Number1} and {Number2} is {IntQuot}")