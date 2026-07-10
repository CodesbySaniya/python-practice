
for x in range(1,11):
  print(x)
print("HAPPY BIRTHDAY!")


#to reverse
for x in reversed(range(1,11)):
 print(x)
print("HAPPY BIRTHDAY!")

#to take a step
for i in range(1,21,):
  print(i)

pin_num="5678-0000-4500-8953"
for i in pin_num:
  print(i)

for x in range(1,21):
  if x == 7:
    continue#use to skip value only
  else:
    print(x)

for x in range(1,21):
  if x == 7:
    break#use to terminate whole prgoram
  else:
    print(x)
