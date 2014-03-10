def calculate(number):
    newnumber = number / 100
    return (newnumber)

for x in range(5,101,5):
    y = calculate(x)
    print(x,"% = ",y)
    
