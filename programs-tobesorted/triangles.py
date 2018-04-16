# this program takes in three numerical values, sorts them into ascending order
# and determines if a triangle can be formed. If a triangle can be formed it
# will determine if it is equilateral, isosceles oe scalene. An appropriate
# message is displayed. 

# enter three lengths
sideA = int(input("Please enter length of side 1 "))
sideB = int(input("Please enter length of side 2 "))
sideC = int(input("Please enter length of side 3 "))

#sort into ascending order
if sideA > sideB:
    temp = sideA
    sideA = sideB
    sideB = temp
if sideB>sideC:
    temp = sideB
    sideB = sideC
    sideC = temp
if sideA > sideB:
    temp = sideA
    sideA = sideB
    sideB = temp

# print lengths in ascending order
print'The lengths of the sides in ascending order are:'
print'side A = ',sideA
print'side B = ',sideB
print'side C = ',sideC

# determine if a triangle can be formed
if sideA + sideB <= sideC:
    print('A triangle cannot be formed with the lengths entered.')
    
# if a triangle can be formed then determine what type it is
elif sideA == sideC:
    print('This is an equilateral triangle')
elif sideA == sideB or sideB == sideC:
    print('This is an isosceles triangle')
else:
    print('This is a scalene triangle')
    

