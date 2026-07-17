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


fruits = {"mango","cherry","strawberry"}#set is also iterable

for fruit in fruits:
  print(fruit)

my_dict = {"A" : 1 ,"B" : 2 , "C" : 3}
for key in my_dict:
  print(key)

for value in my_dict.values():
  print(value)

for item in my_dict.items():
  print(item)
