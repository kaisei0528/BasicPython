
import math



def trapezoidal_integration(f, a=0,b=1,n=100):
    h = (b - a) / n
    integral_sum = 0
   
    for i in range(1,n + 1):
           x1 = a + (i - 1) * h
           x2 = a + i * h
           integral_sum += (f(x1) + f(x2)) / 2
        
    integral_value = h * integral_sum
    return integral_value

#(1)の解答

from math import sin
from math import pi

# --example--
# print(sin(0))

# -----------


a = 0
b=(math.pi)/2
n=50
f1 = math.sin
a1 = trapezoidal_integration(f1,a,b,n)
print(a1)


#(2)の解答
a = 0
b = 1
n = 100
def f2(x):
      return 4 / (1 + (x**2))
a2 = trapezoidal_integration(f2,a,b,n)
print(a2)


#(3)
a = -100
b = 100
n = 1000
def f3(x):
      return ((math.pi)**(1/2)) * (math.e**(-x**2))
a3 = trapezoidal_integration(f3,a,b,n)
print(a3)

           
           




