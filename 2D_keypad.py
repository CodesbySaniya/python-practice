#2d keypad

nums1= [1,2,3]
nums2= [4,5,6]
nums3 = [7,8,9]
nums4 = ["*",0,"#"]

keypad = [nums1,nums2,nums3,nums4]
for num in keypad:
  for i in num:
   print(i, end=" ")
  print()
