#!f:
#filename: functions.py

import os

global total,choice

#def test(points):
    
   

    #points = 0
    #question1(points)
    #question2()
    #question3()
    #question4()
    #print('You scored ', points, ' points.')
    #return(points)

def clear():
  
    for i in range(120):
       print()

    return

def story():
    print('Once upon a time, there were 3 little pigs. There was a scary ')
    print('wolf who kept blowing their house down. So the first pig built a house of straw.')
    print('The second pig built a house of clay and the third built a house of bricks.')
    print('The cheapest - the straw one- blew away in a storm, the next cheapest went running down the hill when it rained.')
    print('But the brick one lasted the longest')
    print('Press <enter> to begin the test')
    keypressed = input()
    print(keypressed)
    while len(keypressed) != 0:
        print('Press <enter> to begin the test')
        keypressed = input()
    clear()
    return




def test(x):
    
     
    print('How many pigs were there? ')
    print('1. one?')
    print('2. two?')
    print('3. three?')
    print('4. none?')
    answer = int(input())
    if answer in [1,2,3,4]:
            if answer == 1:
               print('wrong')
            elif answer == 2:
               print('wrong')
            elif answer == 3:
                y = x + 1
                print(y)
            elif answer == 4:
                print('wrong')
    return


def score(points):

    
    
    print('You scored ', points,'points.')
    return

def menu():

    global choice
    
   
    print('Main Menu')
    print('1. Story')
    print('2. Test')
    print('3. Score')
    print('4. Quit')
    print('Please choose 1 to 4')
    choice = int(input())
    return

def userchoice():
   
    while choice != 4:
        menu()
        if choice in [1,2,3,4]:
            if choice == 1:
                story()
            elif choice == 2:
                test(total)
                print(total)
            elif choice == 3:
                score(total)
            elif choice == 4:
                print('goodbye')
        else:
            print('invalid choice')
    return
    
choice, total = 0,0
userchoice()

            
        
