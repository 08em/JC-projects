# 1a) 
Animals = [None for i in range(10)]

# b)
for i in range(10):
    animals = input("enter animal: ").lower()

# c)
arrayLength = 10

def sortDescending():
    global arrayLength
    for x in range(arrayLength-1):
        for y in range(arrayLength-x-1):
            string1 = animals[y]
            string2 = animals[x]
            if string1[0][1] < string2[0][1]:
                temp = animals[y]
                animals[y] = animals[y+1]
                animals[y+1] = temp

# d) i.
sortDescending()
print(animals)

# ii. screenshot

