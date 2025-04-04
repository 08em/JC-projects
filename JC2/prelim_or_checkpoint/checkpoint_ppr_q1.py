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

# d)
AllEmployees = [Employee("",0,"") for i in range(10)] # of class Employee
file = open("JC2/EmployeeFile.txt", 'r')
for i in range(10):
    AllEmployees[i].__Name = file.readline().strip()
    AllEmployees[i].__EmployeeID = file.readline().strip()
    AllEmployees[i].__Department = file.readline().strip()
