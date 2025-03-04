# 4 pillars of oop : abstraction (only getting the important info), encapsulation (used for data hiding?grp together all the data and actions abt the data), 
# an object is an instance of a class. a class can have any number of objects/instances
# instantiation / instantiate = creating/constructing an instance/object of a class
# constructor = special method  written inside the class used to construct the objects. allows you to create personalized objects instead of default objects

class Car :         # ALWAYS start with capital lerrer for defining class
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
