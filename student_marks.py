#average marks of a student
marks=[]
n=int(input("enter number of subject"))
for i in range(n):
   m=int(input("enter marks:"))
   marks.append(m)
average=sum(marks)/len(marks)
print("average marks",average)
print("maximum marks",max(marks))
print("minimum marks",min(marks))
