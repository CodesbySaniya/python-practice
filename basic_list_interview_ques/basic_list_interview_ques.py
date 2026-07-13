#sum of all elemnts

numbers = [12, 8, 15, 20, 5]

total = 0 
for num in numbers:
  total=total+num
print(total)

#find the largest number

numbers = [45, 12, 89, 23, 67]
largest= numbers[0]

for num in numbers:
  if num > largest:
    largest = num
  elif num<largest:
    largest= largest

print(largest)



#find the smallest number

numbers = [45, 12,-5, 89, 23,-5, 67]
smallest = numbers[0]

for num in numbers:
  if num < smallest:
    smallest = num

print(smallest)


#print(total even numbers and odd numbers)

numbers = [10, 15, 20, 25, 30, 35]
even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0

for num in numbers:
  if num % 2 == 0:
    even_count+=1
    even_sum += num

  elif num % 2 != 0:
    odd_count +=1
    odd_sum += num

print(f"total even numbers are {even_count}")
print(f"sum of total even numbers are {even_sum}")
print(f"total odd numbers are {odd_count}")
print(f"sum of total odd numbers are {odd_sum}")


#reverse a list
numbers = [1, 2, 3, 4, 5]

rev_list = []

for num in numbers:
    rev_list = [num] + rev_list

print(rev_list)
