import random
n=random.randint(1,100)
while True:
  x=int(input("please enter a number"))
  if (x<n):
      print("too low")
  elif (x>n):
      print("too high")
  else:
      print("success")
      break    
