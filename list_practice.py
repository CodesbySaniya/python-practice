# Basic operations on Python List
subject=["science","maths","english","hindi","gk","computer"]
print(subject)
print(subject[2])
print(subject[3])
subject[2]="sst"
print(subject)
print(subject[0:4])
print(subject[:-1])
#list methods
subject.reverse()
print(subject)
subject.append("msc")
print(subject)
subject.insert(3,"supw")
print(subject)
subject.pop()
print(subject)
subject.remove("hindi")
print(subject)
subject.sort()
print(subject)
print(max(subject))
print(len(subject))
