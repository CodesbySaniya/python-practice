#match case statement(switch): an alternative to use many elif condition execute some code if a value match "case"

def day_of_week(day):
  match day:
    case 1:
      return "It is Sunday"
    case 2:
      return "It is Monday"
    case 3:
      return "It is Tuesday"
    case 4:
      return "It is Wednesday"
    case 5:
      return "It is Thursday"
    case 6 :
      return "It is Friday"
    case 7:
      return "It is Satueday"
    case _:
      return "Invalid day"

print(day_of_week((2)))

