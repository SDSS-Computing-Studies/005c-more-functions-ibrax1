#!python3

"""
Create a function that determines the area of a circle if given the radius
1 input parameter
float: radius

return: float area for the circle

note: Area of a circle is given by A = pi*(square of the radius)
You may want to use the math module to complete this problem
"""
import math
x = float(input("Enter Radius: "))
def area(x):
    ar = (x**2)*math.pi
    return(ar)
y = area(x)
print (round (y, 2))

assert round(area(2),2) == 12.57