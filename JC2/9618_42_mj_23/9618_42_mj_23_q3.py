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
class Manager(Employee) :
    def __init__(self, hrlyPay, EmpNo, jobT, bonusVal):
        super.__init__(hrlyPay, EmpNo, jobT)
        self.__BonusValue = bonusVal # real

# ii.
    def SetPay(self, WkNo, HrsWorked):
        bonus = (1 + self.__BonusValue / 100) * HrsWorked
        super().setPay(WkNo, bonus)

# c) i. 
EmployeeArray = [None for i in range(8)]
try :
    file = open("JC2/Employees.txt", 'r')
    for i in range(8):
        hrPay = float(file.readline().strip())
        empNo = file.readline().strip()
        bonusortitle = file.readline().strip() # edit this

        try :
            bonus = float(bonusortitle)
            jobT = file.readline().strip()
            EmployeeArray[i] = Manager(hrPay, empNo, jobT, bonus)

        except :
            jobT = bonusortitle
            EmployeeArray[i] = Employee(hrPay, empNo, jobT)

    file.close()
except FileNotFoundError :
    print("error, file not found")

# d)

def EnterHours():
    try:
        file = open("JC2/HoursWeek1.txt", 'r')
        for i in range(8) :
            employeeNo = file.readline().strip()
            hours = file.readline().strip()

            for x in range(8) :
                if EmployeeArray[x].getEmployeeNumber() == employeeNo :
                    EmployeeArray[x].setPay(1, hours)
                    break 

    except FileNotFoundError :
        print("file not found")

#  e) i.
EnterHours()
for i in range(8) :
    employeeNum = EmployeeArray[i].getEmployeeNumber()
    totalPay = EmployeeArray[i].GetTotalPay()
    print(employeeNum, " ", totalPay)