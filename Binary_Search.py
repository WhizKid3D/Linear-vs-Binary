Number_List = list(range(1,101))

guess = 0
index = 0
target = input("Enter a number ")

if int(target) > .5*(len(Number_List)):
  for number in range(0,50):
    Number_List.pop(0)
  print(Number_List)
  print("hello")
else:
  for number in range(0,51):
    Number_List.pop(number)
  print(Number_List)