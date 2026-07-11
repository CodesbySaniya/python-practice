# *
# **
# ***
# ****
# *****

for i in range(1,6):#decide how many rows
  for x in range(i):#decide how many stars in that row
      print("*",end="")
  print()



# Print the following pattern:

# *****
# *****
# *****
# *****
# *****

for i in range(5):
  for x in range(5):
    print("*",end="")
  print()

# Now print this pattern:

# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
  for j in range(1,i+1):
    print(j,end="")
  print()


# *****
# ****
# ***
# **
# *


for i in reversed(range(1,6)):
  for j in range(i):
    print("*",end="")
  print()
