#python compound interest calculator
principal = 0
time = 0
rate = 0

while principal <= 0:
  principal =float(input("enter the principal amount: "))
  if principal <= 0:
    print("principal cant be less than or equal to zero")

while rate <= 0:
  rate =float(input("enter the interest rate: "))
  if rate <= 0:
    print("interest rate cant be less than or equal to zero")

while time <= 0:
  time =int(input("enter the time(in years): "))
  if time <= 0:
    print("time cant be less than or equal to zero")

total = principal * pow((1 + rate /100),time)
print(f"your balance after {time} is Rs{total:.2f}")
