count = 0
while count <= 10 :
    print(f"{count}: my name is Khan")
    count = count + 1

sum = 0
num = int(input("enter number : "))
while num != -999 : 
        sum = sum + num

print(f"the sum is {sum}")

# algorithm to input numbers until rogue value is input n find sum of all positive numbers from the input
sum = 0
num = int(input("enter number : "))
while num != -999 : 
    if num > 0:
        sum = sum + num

print(f"the sum is {sum}")
