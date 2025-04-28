# 1a) 
animals = ["" for i in range(10)]

# b)
for i in range(10):
    animals[i] = input("enter animal: ").lower()

# c)
arrayLength = 10

def sortDescending():
    global arrayLength
    for x in range(arrayLength-1):
        for y in range(arrayLength-x-1):
            string1 = animals[y]
            string2 = animals[y+1]
            if string1[0] < string2[0]:
                temp = animals[y]
                animals[y] = animals[y+1]
                animals[y+1] = temp

# d) i.
sortDescending()
for i in range(10):
 print(animals[i])

# ii. screenshot

