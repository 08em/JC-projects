Num = int(input("Enter a digit between 1 and 7:"))

if Num == 1:
    print("Sunday")
elif Num == 2:
    print("Monday")
elif Num == 3:
    print("Tuesday")
elif Num == 4:
    print("Wednesday")
elif Num == 5:
    print("Thursday")
elif Num == 6:
    print("Friday")
elif Num == 7:
    print("Saturday")

match Num :
    case 1: print("It is Sunday")
    case 2: print("It is Monday")
    case 3: print("It is Tuesday")
    case 4: print("It is Wednesday")
    case 5: print("It is Thursday")
    case 6: print("It is Friday")
    case 7: print("It is Saturday")
    case _: print("Error, invalid day number")
    # _ is for otherwise


