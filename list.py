#list(basic to advance)

numbers = [10 , 20 , 30 , 40, 50]
print(numbers[0])#indexing
print(numbers[2])
print(numbers[-1])

numbers[2]=300#updating
print(numbers)

numbers = [10 , 20 , 30 , 40, 50]
print(numbers[0:3])#slicing
print(numbers[-1:-3:-1])#in reverse order
#list(basic to advance)

numbers = [10 , 20 , 30 , 40, 50]
print(numbers[0])#indexing
print(numbers[2])
print(numbers[-1])

numbers[2]=300#updating
print(numbers)

numbers = [10 , 20 , 30 , 40, 50]
print(numbers[0:3])#slicing
print(numbers[-1:-3:-1])#in reverse
print(numbers[-2:])#or
print(numbers[3:])#or
print(numbers[1:4])


# Ask the user to enter five numbers. Store them in a list and print:

# The complete list
# The largest number
# The smallest number

num = []

nums = int(input("enter any five num: "))

for nums in range(5):
 nums =int(input("enter any five num or( q to quit )"))
 num.append(nums)
print(num)
print(max(num))
print(min(num))



# Ask the user to keep entering numbers until they type "q". Store all numbers in a list. At the end, print:

# All numbers
# Total
# Average

list1 = []
total = 0
avg = 0



while True:
  num=input("enter numbers u want or q to quit : ").lower()
  if num =="q":
    break
  else:
   b = int(num)
   list1.append(b)
   total += b
   avg = total / len(list1)
  
  
print(list1)
print(total)
print(avg)

