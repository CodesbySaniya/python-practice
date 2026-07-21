#variable scope - where a variable is accessible and visible
#scope resolution - local > enclosed -> global -> built in (LEGB)

#LOCAL SCOPE
def var1():
  x=2         #LOCAL SCOPE WRITTEN INSIDE A FUNCTION
  print(x)

def var2():
  x=3
  print(x)    #WE CANNOT USE LOCAL VARIABLE IN ANOTHER FUNCTION

var1()
var2()
