# python to calculate area of a circle
PI = 3.14159

Radius = float(input("please enter the radius of a circle : "))
if Radius <= 0 : 
   print("radius cannot be less than or equal to 0, please input another value:")
else :
    Area = PI * Radius * Radius
    print(f"the area of a circle with radius {Radius} is {Area}") 
