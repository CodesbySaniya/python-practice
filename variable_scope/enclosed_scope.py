#variable scope - where a variable is accessible and visible
#scope resolution - local > enclosed -> global -> built in (LEGB)

#ENCLOSED SCOPE
def var1():
  x=2         #ENCLOSED SCOPE WRITTEN INSIDE A NOTHER FUNCTION
  def var2():
   print(x) 
  var2()
var1()
