userInput = int(input("How many items would you like in the array?: "))
array = []
printStr = ""
total = 0
print()

for i in range(0, userInput):
    userValue = input("Value " + str(i+1) + ": ")
    array.append(userValue)

for i in array:
    printStr += (i + ". ")

for i in range(0, len(array)):
    total += int(array[i])

print()
print("Your array is: " + printStr)
print("The total of your array is: " + str(total))
