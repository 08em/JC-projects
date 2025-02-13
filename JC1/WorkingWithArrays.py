StudentNames = [None for counter in range(10)] # StudentNames is str array of 10 elements 
# this is how to declare array in python (no arrays in python, so we use list)
StudentMarks = [0 for counter in range(10)]

for counter in range(10):
    StudentNames[counter] = input("enter student name:")
    StudentMarks[counter] = input("enter student marks:")

for counter in range(10):
    print(StudentNames[counter])

print(StudentNames)
print(StudentMarks)

# or
# for index in range(10):
#   print(StudentNames[index])
#   print(StudentNames[index])

found = False
searchStudent = input("please enter student name to search:")
for index in range(10):
    if searchStudent == StudentNames[index]:
        found = True
        position = index

if found == True:
    print(f"{searchStudent} found and student has scored {StudentMarks[position]}")
else:
    print(f"{searchStudent} not found")
