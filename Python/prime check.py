inputNum = int(input("Pick any number "))
prime = True
divide = 0
def primeCheck(numTest):
    global divide,prime
    num = 2
    count = 0
    while count != 100:
        if numTest % num == 0:
            divide += 1
        num += 1
        count += 1

def checkNum(inputNum):
    global divide
    number = inputNum + 1
    primeTotal = 0
    while primeTotal != 100:
        divide = 0
        primeCheck(number)
        if divide < 2:
            prime = False
        elif divide > 2:
            prime = True
        if prime == False:
            print(number)
            primeTotal += 1
        number += 1

primeCheck(inputNum)
if divide < 2:
    prime = False
elif divide > 2:
    prime = True
if prime == False:
    print("The number is prime!")
elif prime == True:
    print("The number is not prime!")


checkNum(inputNum)

