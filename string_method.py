#IMPORTANT FUNCTIONS

name = input("Enter the full name: ")
phone_number =(input('Enter phone number: '))
result=len(name)
result=name.find(" ")#finds first occurence
result = name.rfind("a")#finds last occurrence
result=name.capitalize()
result=name.upper()
result=name.lower()
result=name.isdigit()

result = str(phone_number).count("5")
result=phone_number.replace("-","  ")
print(result)

print(help(str))
