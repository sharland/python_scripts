#!/usr/bin/python
# -*- coding: utf-8 -*-


def print_menu():
    print 'make a choice'
    print '1. Print phone number'
    print '2. add a new phone number'
    print '3. remove an exisiting phone number'
    print '4. look up a phone number'
    print '5. quit'
    print ()


numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input('choose an option (1-5): '))
    if menu_choice == 1:
        print 'listing of telephone numbers:'
        for x in numbers.keys():
            print ('name: ', x, '\tnumber:', numbers[x])
            print ()
    elif menu_choice == 2:
        print 'adding a new name & number:'
        name = input('name: ')
        phone = input('number:')
        numbers[name] = phone
        print ('successfully added a new name and number for', name)
    elif menu_choice == 3:
        print 'removing name and number from the dictionary'
        name = input('name: ')
        if name in numbers:
            del numbers[name]
            print ('successfully removed name and number for', name)
        else:
            print (name, 'was not found')
    elif menu_choice == 4:
        print 'Lookup a number from a name'
        name = input('Name; ')
        if name in numbers:
            print ('The number is', numbers[name])
        else:
            print (name, 'was not found')
    elif menu_choice != 5:
        print_menu()
