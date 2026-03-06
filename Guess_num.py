#guess the number
import random

target=random.randint(1,100)

while True:
  userchoice=input("enter the number you want to guess or quit(Q)")
  if(userchoice=="quit" or userchoice=="Q"):
    print("you quit the game")
    break

  userchoice=int(userchoice)
  if(target==userchoice):
    print("you chose a correct number")
    break

  elif(target>userchoice):
    print("take a bigger guess")

  else:
    print("take a smaller guess")

print("---*GAME OVER*---")
