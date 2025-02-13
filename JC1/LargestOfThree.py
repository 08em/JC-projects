Num1 = int(input("enter first number:"))
Num2 = int(input("enter second number:"))
Num3 = int(input("enter third number:"))

if Num1 > Num2 :
    if Num1 > Num3 :
        print(f"{Num1} is the largest")
    else :
        print(f"{Num3} is the largest")
elif Num2 > Num3 :
        print(f"{Num2} is the largest")
else :
        print(f"{Num3} is the largest")
