#iterable - a collection / object that can iterate over a loop

numbers = [1,2,3,4,5] #list is iterable

for number in reversed(numbers):
  print(number ,  end = " - ")

numbers = (1,2,3,4,5) #tuples are iterable

for item in reversed(numbers):
  print(item)

name = "saniya" #string is also iterable

for name in name:
  print(name)
