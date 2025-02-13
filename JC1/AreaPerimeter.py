# program to calculate the area or perimeter of a circle.
# use procedures and/or functions for each of the following tasks :
# 1. input and validate the radius
# 2. calculate the area
# 3. calculate the perimeter
# 4. output the result
# in the main program should give user the choice to calculate area or perimeter

pi = 3.14


def validateRad() :
    radius = float(input("enter radius of the circle: "))
    if radius <= 0 :
        print("error, radius should be more than 0")
        radius = float(input("reinput radius : "))
    else :
        return radius


def areaOfCircle() :
    area = pi*radiusCircle*radiusCircle
    return area

def perimeterOfCircle() :
    peri = 2*pi*radiusCircle
    return peri

radiusCircle = validateRad()

choice = input("calculate area or perimeter?")

match choice :
    case "area" : print(areaOfCircle())
    case "perimeter" : print(perimeterOfCircle())    