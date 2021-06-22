#!python3
"""
Create a function that converts from degrees F to degrees C or
vice versa, depending on which initial unit is given
2 input parameters:
float: the number of degrees
string: the unit that you currently have: may be 'C' of 'F'

return: float the number of degrees of the other unit

Sample assertions:
assert convertTemp(10,'C') == 50
assert converTemp(32,'F') == 0
"""

temp = float(input("enter the temperature value: "))
degrees = input ("Enter the unit (C or F): ")

def convertTemp(temp, degrees):
    if degrees == "C" or "c":
        f = (temp* (9/5) +32)
        return(f)
    else:
        c = ((temp - 32)*(5/9))
        return(c)
x = convertTemp(temp, degrees)
print(x)