myfirstname=input("Enter your first name: ")    #An input request asking for a first name
myage=int(input("Enter your age: "))            #an input request asking for age and storing it as an integer
if myfirstname=="Brian":                        #beginning of an if request testing if input is equal to "brian"
    print ("Hello " + myfirstname)              #prints a string and the value of the variable myfirstname             
    myage=myage+1                               #redefines myage as the original variable value plus one
    print ("Next year you will be",myage)       #prints a string plus the newly redefined myage
else:                                           #starts the else when the if fails
    print ("try again")                         #prints a simple string
