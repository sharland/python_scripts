currentNumber = int(input("Input integer: "))
runningTotal = currentNumber

while currentNumber > 0:
    currentNumber = currentNumber - 1
    runningTotal = currentNumber * runningTotal
    print(runningTotal)
