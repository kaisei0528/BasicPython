import math
from fractions import Fraction
import cmath

a = 1
b = -6
c = 9

d = 2
e = -8

f = 8
g = -6
h = -35

i = 1j



# TODO


#(1)
x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
#(2)
x2 = (-d + math.sqrt(d**2 - 4*a*e)) / (2*a)
x3 = (-d - math.sqrt(d**2 - 4*a*e)) / (2*a)
#(3)
x4 = (-g + math.sqrt(g**2 - 4*f*h)) / (2*f)
x5 = (-g - math.sqrt(g**2 - 4*f*h)) / (2*f)

fraction_x4 = Fraction(x4).limit_denominator()
fraction_x5 = Fraction(x5).limit_denominator()

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)

#(4)

a = 1
b = 0 
c = 1


x6 = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
x7 = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)

print(x6)
print(x7)



