# 1a)
class Employee:
    def __init__(self, Name, EmployeeID, Department): # ask if shld be only __init__ or follow qs ppr
        self.__Name = Name
        self.__EmployeeID = EmployeeID
        self.__Department = Department
# b)
    def GetName(self):
        return self.__Name
    
    def GetEmployeeID(self):
        return self.__EmployeeID
    
    def GetDepartment(self):
        return self.__Department
# c)  
    def ChangeDepartment(self, NewDepartment):
        self.__Department = NewDepartment

    def setName(self, Name) :
        self.__Name = Name

    def setEmployeeID(self, EmployeeID) :
        self.__EmployeeID = EmployeeID

    def setDepartment(self, Department) :
        self.__Department = Department
# d)
AllEmployees = [Employee("",0,"") for i in range(10)] # of class Employee
file = open("JC2/EmployeeFile.txt", 'r')
# line = file.readline().strip()
i = 0
# while line != "":
#     AllEmployees[i].setName(line)
#     line = file.readline().strip()
#     AllEmployees[i].setEmployeeID(line)
#     line = file.readline().strip()
#     AllEmployees[i].setDepartment(line)
#     line = file.readline().strip()
#     i = i + 1

# for i in range(len(AllEmployees)):
#     print(AllEmployees[i].GetName(), AllEmployees[i].GetEmployeeID(), AllEmployees[i].GetDepartment())

for i in range(10):
    AllEmployees[i].setName(file.readline().strip())
    AllEmployees[i].setEmployeeID( file.readline().strip())
    AllEmployees[i].setDepartment( file.readline().strip())

# e)
search = input("enter name to search for: ")
found = False
while found == False:
    for i in range(10):
        if search == AllEmployees[i].GetName() :
            index = i
            found = True
        
        if found == False and i == 10 :
            search = input("name not found, enter another name to search for: ")

# f) 
action = input("enter P to print employee's information, enter D to change employee's department: ")
if action != "P" or action != "D":
    print("invalid input, please enter either P or D")
    action = input("enter P to print employee's information, enter D to change employee's department: ")

if action == 'P':
    print(AllEmployees[index].GetName(), AllEmployees[index].GetEmployeeID(), AllEmployees[index].GetDepartment())
else:
    newDept = input("enter the new department of employee: ")
    AllEmployees[index].ChangeDepartment(newDept)

