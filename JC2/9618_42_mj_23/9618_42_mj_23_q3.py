# 3a) i.
class Employee :
    def __init__(self, hrlyPay, EmpNo, JobT):
        self.__HourlyPay = hrlyPay # real
        self.__EmployeeNumber = EmpNo # string
        self.__JobTitle = JobT # string
        self.__PayYear2022 = [0.0 for i in range(52)] # real
    
# ii. 
    def getEmployeeNumber(self):
        return self.__EmployeeNumber
    
# iii. 
    def setPay(self, WkNo, HrsWorked):
        self.__PayYear2022[WkNo] = HrsWorked * self.__HourlyPay

# iv. 
    def GetTotalPay(self):
        return self.__PayYear2022
    
# b) i.
class Manager :
    def __init__(self, hrlyPay, EmpNo, jobT, bonusVal):
        super.__init__(hrlyPay, EmpNo, jobT)
        self.__BonusValue = bonusVal # real

# ii.
    def SetPay(self, WkNo, HrsWorked):
        bonus = self.__BonusValue * HrsWorked
        self.__PayYear2022[WkNo] = self.__PayYear2022[WkNo] + bonus

# c) i. 
EmployeeArray = [Employee(0.0, "", "", 0.0) for i in range(8)]
file = open("JC2/Employees.txt", 'r')
for i in range(8):
    hrPay = file.readline().strip()
    empNo = file.readline().strip()
    jobT = file.readline().strip() # edit this
    EmployeeArray[i] = Employee(hrPay, empNo, jobT)