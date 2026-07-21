# import math
# import math as m
from math import pi
print(pi)

from math import e
print(e)

from math import log
print(log(2))


#saniya module
pi = 3.1459

def square(x):
  return x**2

def cube(x):
  return x**3

def circumference(radius):
  return 2*pi*radius

def area(radius):
  return pi * radius**2

import saniya

result = saniya.area(5)
result = saniya.square(5)
result = saniya.cube(5)
result = saniya.circumference(5)
print(result)
