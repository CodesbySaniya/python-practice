#triangle area using heron's formula
import math
a=float(input("enter side a:"))
b=float(input("enter side b:"))
c=float(input("enter side c:"))
s=a+b+c/2
area=math.sqrt((s-a)*(s-b)*(s-c))
print(area)
