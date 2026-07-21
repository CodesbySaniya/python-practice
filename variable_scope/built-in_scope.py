#variable scope - where a variable is accessible and visible
#scope resolution - local > enclosed -> global -> built in (LEGB)

#BUILT-IN SCOPE

from math import e #BUILT-IN VERSION OF e

def fun1():
  print(e)

e = 3 #GLOBAL VERSION OF e

fun1() #will print e=3 bcoz scope resolution - local -> enclosed -> global -> built in (LEGB)
