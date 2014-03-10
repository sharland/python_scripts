#This is the procedure being defined
def output(number):
    print(number, "squared =",number*number)

#This is the main program which uses that procedure
x = 1

while x < 21:
    output(x)
    x = x + 1
    
