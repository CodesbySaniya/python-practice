#default argument
def detail(name , branch="ce" , year=3):
  return  f" your name: {name} \n your branch: {branch}  \n year:  {year} "

print(detail("saniya"))


#keyword argument (posotion of argument doesnt matter)

def detail(name , branch, year): #default argument
  return  f"your name: {name} ,  your branch: {branch}  , year:  {year} "

print(detail(name = "saniya",year = "3rd",branch = "cse"))

# #arbitary argument stores multiple non key values #we use tuple
def add(*args):
  total = 0
  for arg in args:
    total +=arg
  return total

print(add(2,3,5,6))

def name(*args):
  for arg in args:
    print(arg , end=" ")
  

print(name("saniya","neha"))

#keyword arbitary argument type - dictionary and can store multiple kyeywords

def detail(**kwargs):
  for key,value in kwargs.items():
    print(f"{key}:{value}")

detail(
    name="saniya", 
    branch="cse",
    year="3rd")
