#TERNARY OPERATOR( a one line short cut for if else)
# returns X if condition else Y
num = float(input("enter your marks to check whether youare pass or fail: "))
print("you have passed the exam ,congrats!" if num >= 33 else "you did not passed the exam")

#example-2

age= int(input("Enter your age: "))

print("you are eligible to vote" if age >= 18 else "you are not eligible to vote")

#example-3 even or odd
num = int(input("enter the number to knoe whether it is even or odd: "))
print("Number is even" if num % 2 == 0  else "Number is odd")
