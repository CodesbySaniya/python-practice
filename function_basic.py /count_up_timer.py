def timer(start,end=9):
  for x in range(start,end+1):
    print(x)
    time.sleep(1)
  print("Time's up!")

timer(1)
