Number_List = list(range(1,101))

guess = 0
index = 0
target = input("Enter a number ")

for number in Number_List:
  guess += 1

  if int(target) == Number_List[index]:
    print(str(guess) + " was guessed in " + str(guess) + " guesses!")
  index += 1