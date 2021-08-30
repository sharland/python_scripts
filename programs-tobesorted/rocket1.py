#!f:
#filename: rocket1.py
def drawtop():
    print('   /\   ')
    print('  /  \  ')
    print(' /    \ ')
    print(' ------ ')
    return
def drawbox():
    print(' ------ ')
    print('|      |')
    print('|      |')
    print(' ------ ')
    return
def drawexhaust():
    print(' |   |  ')
    print()
    return

def drawrocket():
    drawtop()
    for i in range(1,3):
        drawbox()
    for i in range(1,200):
        drawexhaust()
    return
    

def menu():

    global choice
    print('Do you wish to draw:-')
    print('1. a triangle?')
    print('2. a square?')
    print('3. a rocket?')
    print('4. Quit?')
    print('choose 1 to 4')
    choice = int(input())
    return

def userchoice():

    while choice != 4:
        menu()
        if choice in [1,2,3,4]:
            if choice == 1:
                drawtop()
            elif choice == 2:
                drawbox()
            elif choice == 3:
                drawrocket()
            else: 
                print('goodbye')
        else:
            print('invalid choice')
    return
    
choice = 0
userchoice()

            
        
