#default argument
def detail(name , branch="ce" , year=3):
  return  f" your name: {name} \n your branch: {branch}  \n year:  {year} "

print(detail("saniya"))


#keyword argument (posotion of argument doesnt matter)

def detail(name , branch, year): #default argument
  return  f"your name: {name} ,  your branch: {branch}  , year:  {year} "

print(detail(name = "saniya",year = "3rd",branch = "cse"))
