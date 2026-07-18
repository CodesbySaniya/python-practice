#print 1 to 5 using loop
num=1
while num <= 5:
 print(num)
 num+=1

#print only even number
list1 = [3, 8, 11, 14, 17,43,52,78,65,41,-75,98,20]
list2=[]
for i in list1:
  if i % 2 == 0:
    list2.append(i)
print(list2)
