password = input("Enter password: ")
attempt =3

while password != "python123":
  print("Wrong password !")
  attempt=attempt-1
  print("Attempt left: ",attempt)
  password = input("Enter password: ")
  if attempt == 0:
    print("account locked !")
    break

if password == "python123":
  print("Access Granted")
