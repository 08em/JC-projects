class Car :         # ALWAYS start with capital letter for defining class
    def __init__(self, make, model, color):     # python calls constructor an initializer
        self.make = make
        self.model = model
        self.color = color

    def start(self): # self refers to object itself
        print("car has started")

    def stop(self):
        print("car has stopped")

# car1 = Car() # parentheses is a default blank constructor made by python
# car1.make = "toyota"
# car1.model = "2001"
# car1.color = "red"
# above doesnt work anymore because the default blank constructor doesnt work anymore

car1 = Car("Toyota", "2001", "red") # instantiation
car2 = Car("BMW", "2023", "black") # instantiation
print(car1.make)
print(car1.model)
print(car1.color)
car1.start() # python passes car1 as an argument into the function, which is what causes the error if you dont put self as an arg during declaration
car1.stop()

car2 = Car("honda", "2021", "black")

class Person:
    personCount = 0  # this is a class variable

    def __init__(self, name, DoB, gender):
        self.__name = name # of type string ; the double underscore bfr name makes the var turn from public to private, so it is now no longer visible
        self.__DoB = DoB # of type date
        self.__gender = gender # of type string
        Person.personCount += 1
    
    # name, dob, and gender are called instance/object variables

    def walk(self):
        print("person is walking")

    def run(self):
        print("person is running")

    #getters and setters
    def getName(self):
        return self.__name
    
    def getDoB(self):
        return self.__DoB
    
    def getGender(self):
        return self.__gender
    
    def setName(self, newName):
        self.__name = newName
    
    def printDetails(self):
        print(f"Name: {self.__name}, DoB: {self.__DoB}, Gender: {self.__gender} ")

class Teacher(Person):
    def __init__(self, name, DoB, gender, salary):
        super().__init__(name, DoB, gender)
        self.salary = salary

    def printDetails(self):
        print(f"Name: {self.getName()}, DoB: {self.getDoB()}, Gender: {self.getGender()}, Salary : {self.salary}")

class Student(Person):
    def __init__(self, name, DoB, gender, grade):
        super().__init__(name, DoB, gender)
        self.grade = grade

    def printDetails(self):
        print(f"Name: {self.getName()}, DoB: {self.getDoB()}, Gender: {self.getGender()}, Grade : {self.grade}")


person1 = Person("Shuaib", "20/07/1960", "Male")
person2 = Person("John", "01/02/1999", "Male")
person3 = Person("Aliyah", "03/04/2005", "Female")

# print(person1.__name, person1.__DoB, person1.__gender)
print(person1.getName(), person1.getDoB(), person1.getGender()) 
print(person2.name, person2.DoB, person2.gender)
print(person3.name, person3.DoB, person3.gender)

print(person1.__dict__) # only valid for python

print(Person.personCount)
print(person1.personCount) # doesnt print 1 because personCount is a class variable, so its the same for every object

person1.setName("Alex")
# print(person1.getName(), person1.getDoB(), person1.getGender()) 
person1.printDetails()
person2.printDetails()
person3.printDetails()

teacher1 = Teacher("Allan", "21/12/1990", "Male", 20000)
teacher1.printDetails()

student1 = Student("Amy", "03/08/2000", "Female", 90)

# for reading a file and making it into array of objects where no. of objects is unknown, use :
# file = open("JC2/EmployeeFile.txt", 'r')
# line = file.readline().strip()
# i = 0
# while line != "":
#     AllEmployees[i].setName(line)
#     line = file.readline().strip()
#     AllEmployees[i].setEmployeeID(line)
#     line = file.readline().strip()
#     AllEmployees[i].setDepartment(line)
#     line = file.readline().strip()
#     i = i + 1

# otherwise, if no. of objects is known, just use a for loop