# write a code to find the area and perimeter of :
# 1. circle
# 2. rectangle
# 3. parallelogram
# 4. triangle
# 5. sphere (volume)
# your program must have separate functions for the area and perimeter of each shape

import math

def areaCircle(radius):
    arCircle = math.pi * radius * radius
    return arCircle

def perimeterCircle(radius):
    perCircle = 2 * math.pi * radius
    return perCircle

def areaRectangle(length,breadth) :
    arRectangle = length * breadth
    return arRectangle

def perimeterRectangle(length,breadth):
    perRectangle = length + length + breadth + breadth
    return perRectangle

def areaParallelogram(base, height):
    arParallelogram = base * height
    return arParallelogram

def perimeterParallelogram(length,breadth):
    perParallelogram = length + length + breadth + breadth
    return perParallelogram

def areaTriangle(base, height):
    arTriangle = 0.5 * base * height
    return arTriangle

def perimeterTriangle(side1,side2,side3):
    perTriangle = side1 + side2 + side3
    return perTriangle

def volumeSphere(radius):
    volSphere = 4/3 * math.pi * radius * radius * radius
    return volSphere


def ArPerCircle():
    Rad = float(input("enter radius of circle: "))
    print(f"the area of circle with radius {Rad} is {areaCircle(Rad)} and the perimeter is {perimeterCircle(Rad)}")

def ArPerRectangle():
    len = int(input("enter length of rectangle: "))
    brea = int(input("enter breadth of rectangle: "))
    print(f"the area of the rectangle is {areaRectangle(len,brea)} and the perimeter is {perimeterRectangle(len,brea)}")

def ArPerParallelogram():
    len = int(input("enter length of parallelogram: "))
    brea = int(input("enter breadth of parallelogram: "))
    hei = int(input("enter height of parallelogram: "))
    print(f"the area of the parallelogram is {areaParallelogram(len,hei)} and the perimeter is {perimeterParallelogram(len,brea)}")

def ArPerTriangle():
    bas = int(input("enter base of triangle: "))
    hei = int(input("enter height of triangle: "))
    side = int(input("enter other side of triangle: "))
    print(f"the area of the triangle is {areaTriangle(bas,hei)} and the perimeter is {perimeterTriangle(bas,hei,side)}")

def volSphere():
    Rad = float(input("enter radius of sphere: "))
    print(f"the volume of the sphere with radius {Rad} is {volumeSphere(Rad)} ")

Shape = input("input shape to find area and perimeter: ")
match Shape :
    case "circle": ArPerCircle()
    case "rectangle": ArPerRectangle()
    case "parallelogram": ArPerParallelogram()
    case "triangle": ArPerTriangle()
    case "sphere": volSphere()
    case _: print("Error, invalid shape")