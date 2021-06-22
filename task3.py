#!python3

"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""
import math
s1 = float (input("enter a short side: "))
s2 = float (input("enter another short side: "))
s3 =()
def hypotenuse(s1, s2):
    s3 = (s1**2) + (s2**2)
    s3 = math.sqrt(s3)
    return(s3)
x = hypotenuse(s1, s2)
print(x)
assert hypotenuse(6,8) == 10