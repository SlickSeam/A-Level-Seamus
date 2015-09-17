totalNum = 0
greater = 0
lower = 0
inputNum = 0
even = 0
odd = 0
evenList = []
oddList = []
while inputNum != -999:
    inputNum = int(input("Pick any number "))
    totalNum += 1
    if inputNum > 0:
        greater += 1
    elif inputNum < 0:
        lower += 1
    if inputNum %2 == 0:
        even += 1
        evenList.append(inputNum)
    else:
        odd += 1
        oddList.append(inputNum)
print("")
print(totalNum,"numbers were entered")
print(greater,"numbers were greater than 0")
print(lower,"numbers were lower than 0")
print(even,"numbers were even")
print(odd,"numbers were odd")
print(evenList,"these were the even numbers")
print(oddList,"these were the odd numbers")

