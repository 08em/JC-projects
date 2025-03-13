dictionary = {"England": "London",
              "France" : "Paris",
              "Germany" : "Berlin"}

key = input("enter key: ")

if key in dictionary:
    print(dictionary[key])
else:
    print("not found")


student = {"Name" : "Emily",
          "StudentId" : "0000",
          "Gender" : "Female",
          "Class" : "JC2 Truth"}

studentKey = input("enter student key: ")

if studentKey in student:
    print(student[studentKey])
else:
    print("not found")

student["Age"] = "16"

newKey = input("enter key to be added: ")
newVal = input("enter the value for the key: ")

if newKey in student:
    print("key is already in student dictionary")
else:
    student[newKey] = newVal

print(student)