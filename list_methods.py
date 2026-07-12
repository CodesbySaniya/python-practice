#collection-single variable used to store multiple value

marks=[34,65,34,87,99,34,65,88]
print(marks)
marks.append(54)#ends at last
print(marks)
marks.insert(0,76)#insert at index position we give
print(marks)
marks.pop(1)#pop with index number
print(marks)
marks.copy()
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)
marks.remove(99)#remove with number
print(marks)
marks.clear()#clear lists
print(marks)


numbers = [10,20,30]
numbers.append(40)
numbers.append(50)
print(numbers)

numbers.insert(1,15)
numbers.insert(3,25)
print(numbers)


list1 = [1,2]
list2 = [3,4]

list1.extend(list2)
print(list1)

list1 = [10,20]
list2 = [30,40]
list1.extend(list2)
print(list1)
