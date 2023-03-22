Number_List = list(range(1,101))
print(len(Number_List))
computations = 0
target = input("Enter a number ")

while len(Number_List) > 1:
    #eliminates lower half
    if int(target) > (.5*(len(Number_List))):
        computations += 1
        numlistlen = len(Number_List)
        numlistlen = numlistlen/2
        numlistlen = round(numlistlen)
        for number in range(0,numlistlen):
            Number_List.pop(0)
        #should eliminate upper half
    else:
        computations += 1
        numlistlen = len(Number_List)
        numlistlen = numlistlen/2
        numlistlen = numlistlen - 1
        numlistlen = round(numlistlen)
        for number in range(-1,numlistlen):
            Number_List.pop((len(Number_List))-1)
print(str(target) + " was guessed in " + str(computations) + " computations!")