#LOGICAL OPERATORS (used to evaluate multiple conditions AND, OR ,NOT )

age=6
is_vaccinated= True

if age>=5 and is_vaccinated:
  print("you not need vaccine")

#TEMPRATURE PROGRAM using OR

temp = int(input("Enter the temprature: "))
is_raining = input("Enter yes or no: ").lower()

if temp > 30 or temp < 0 or is_raining == "yes":
  print("event is cancelled")
else:
  print("event is scheduled")

#using NOT

age=29
is_voted=False

if age >=18 and (not is_voted):
  print("you should voted")

else:
  print("you have vote")
