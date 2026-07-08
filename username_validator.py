#username is no more than 12 characters
#username must not contain spaces
#Username must not contain digits

name=input("Enter your username: ")

if len(name) >12:
  print("you cannot use more than 12 characters")

elif any(char.isdigit() for char in name):
  print("Username must not contain digits")

elif " " in name:
  print("Username must not contain space")

else:
  print("username created")
