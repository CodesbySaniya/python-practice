
food = input("what is your fav food( q tp quit)")

while food.lower() != "q":
  print(f"{food} is really a great choice")
  food = input("what is your fav food( q to quit)")
print("you quit")

print("can i order this for you ?")
ans = input("yes or no:")

if ans.lower() == "yes":
  print("I ordered a food for uh..enjoy your food")
else:
  print("no problem sir/mam")
