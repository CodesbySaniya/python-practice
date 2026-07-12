# Write a program to print Hello World.
# Take user name and print greeting.
# Take age as input and check voting eligibility.
# Check whether a number is positive, negative or zero.
# Check whether a number is even or odd.
# Find the largest among two numbers.
# Find the largest among three numbers.
# Create a simple calculator.
# Convert Celsius to Fahrenheit.
# Convert Fahrenheit to Celsius.
# Calculate simple interest.
# Calculate compound interest.
# Check whether a year is leap year.
# Make a username/password validation program.

print("Hello World")

name = input("Enter your username")
print(f"hello {name},have a good day!")

age = int(input("enter your age: "))
print("you are eligible to vote" if age>= 18 else "you are not eligible to vote")

num = int(input("Enter a number to check: "))
if num == 0:
  print("number is zero")
elif num > 0: 
  print("number is postive")
else:
  print("number is negative")

num = int(input("Enter a number to check whether it is even or odd: "))
if num % 2 ==0:
  print("number is even")
else:
  print("number is odd")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1>num2:
  print("first number is greater")
else:
  print("second number is greater")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("First number is largest")
elif num2 >= num1 and num2 >= num3:
    print("Second number is largest")
else:
    print("Third number is largest")

#simple calc
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
symbol = input("Enter symbol(+,-,*,/): ")

if symbol == "+":
  print(num1+num2)

elif symbol == "-":
  print(num1-num2)

elif symbol == "*":
  print(num1*num2)

elif symbol == "/":
  print(num1/num2)

else:
  print("Invalid Syntax")

#convert celsius into farenhiet and farenheit into celsius
temp = int(input("enter the temprature"))
unit = input("enter unit celsius (C) or farenhiet (f): ").lower()


if unit == "c":
  print(f"Temprature in farenheit is{(temp*9/5)+32} f")
elif unit == "f":
  	print(f"Temprature in celsius is {(temp-32)*5/9} celsius")
else:
  print("Invalid Unit")

#calculate si and ci

principal = float(input("Enter principal amount: "))
rate = int(input("Enter rate: "))
time = int(input("Enter a time in year: "))

si = (principal*rate*time)/100
print(f"simple interest for{principal} at {rate} % interest for {time} year is {si}")

ci= principal*((1+rate/100)**time) - principal
print(f"compound interest for{principal} at {rate} % interest for {time} year is {ci}")


#leap year or not
year = int(input("Enter year"))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")

#validate password

correct_password = "saniya123"
password = input("enter password")

while password !=correct_password:
   password = input("Wrong password. Enter again: ")


print("you enter correct password")
