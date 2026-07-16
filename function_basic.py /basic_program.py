#create a function thata returns the square of number
def square(a):
  return a*a
  
print(square(4))


#function

def happy_birthday():
  print("Happy Birthday To You!")
  print("Happy Birthday To You!")
  print("Happy Birthday Dear friend!")
  print("Happy Birthday To You!")
  print()

happy_birthday()
happy_birthday()
happy_birthday()


# functions 

def add(x,y):
  z = x+y
  return z


def subtract(x,y):
  z = x-y
  return z

def multiply(x,y):
  z = x*y
  return z

def divide(x,y):
  z= x/y
  return z

print(add(3,4))
print(subtract(3,4))
print(multiply(3,4))
print(divide(3,4))

def create_name(first,last):
  first = first.capitalize()
  last  = last.capitalize()
  return (first +" "+ last)

print(create_name("saniya","anijwal"))
