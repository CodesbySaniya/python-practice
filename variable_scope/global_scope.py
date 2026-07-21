#variable scope - where a variable is accessible and visible
#scope resolution - local > enclosed -> global -> built in (LEGB)

#GLOBAL SCOPE
def var1():        
  print(x)

def var2():
  print(x) 

x=5          #GLOBAL SCOPE WRITTEN OUTSIDE A FUNCTION

var1()
var2()
print(x)
