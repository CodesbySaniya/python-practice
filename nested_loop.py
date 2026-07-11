#nested loop (loop inside another loop)
#            outer loop:
#                 inner loop:



for x in range(3):#runs 3 time
   for x in range(1,10):
    print(x,end=" ")
   print()



rows = int(input("enter the # of rows: "))
coloumn = int(input("enter the # of coloums: "))
symbol = input("Enter the symbol you want to use: ")
for x in range(rows):
   for x in range(coloumn):
    print(symbol,end=" ")
   print()
