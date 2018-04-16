#!f:
#filename: functions.py

import os



def test():
    
   

    
    question1()
    question2()
    question3()
    question4()
    
    return

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




def question1():
    
    global points
    points = 0
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
                points = points + 1
            elif answer == 4:
                print('wrong')
    return

def question2():

    global points    
    print('How many wolves were there? ')
    print('1. one?')
    print('2. two?')
    print('3. three?')
    print('4. none?')
    answer = int(input())
    if answer in [1,2,3,4]:
            if answer == 1:
                points = points + 1
            elif answer == 2:
                print('wrong')
            elif answer == 3:
                print('wrong')
            elif answer == 4:
                print('wrong')
    return

def question3():

    global points
     
    print('Which was the cheapest house? ')
    print('1. the clay house?')
    print('2. the straw house?')
    print('3. the brick house?')
    print('4. none?')
    answer = int(input())
    if answer in [1,2,3,4]:
            if answer == 1:
                print('wrong')
            elif answer == 2:
                points = points + 1
            elif answer == 3:
                print('wrong')
            elif answer == 4:
                print('wrong')
    return

def question4():

    global points     
    print('Which house lasted the longest? ')
    print('1. the clay house?')
    print('2. the straw house?')
    print('3. the brick house?')
    print('4. none?')
    answer = int(input())
    if answer in [1,2,3,4]:
            if answer == 1:
                print('wrong')
            elif answer == 2:
                print('wrong')
            elif answer == 3:
                points = points + 1
            elif answer == 4:
                print('wrong')
    return

def score():

    global points
    
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

    global choice
    choice = 0
    while choice != 4:
        menu()
        if choice in [1,2,3,4]:
            if choice == 1:
                story()
            elif choice == 2:
                test()
            elif choice == 3:
                score()
            elif choice == 4:
                print('goodbye')
        else:
            print('invalid choice')
    return
    

userchoice()

            
        
