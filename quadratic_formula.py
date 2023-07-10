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

i = 0



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

#(4)
x6 = (-i + cmath.sqrt(i**2 - 4*a*a)) / (2*a)
x7 = (-i - cmath.sqrt(i**2 - 4*a*a)) / (2*a)

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)





