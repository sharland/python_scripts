#Program Name: Card or coin
#Author: D McKenna
#Date created: 10/06/2014
#Description: A small program to produce a random outcome based on
#whether the user choses to pick a card or toss a coin.

#This is the loop that allows the user to play again or exit the program
while True:
    menu = input(
        """
        Y - Play
        N - Exit
        """
        ).casefold()#validates to accept any case
    if menu == "y":


#imports the random function to allow the program to generate random number
        import random

#lists that store the possible suits and values of the cards
        suit = ["Hearts","Diamonds","Spades","Clubs"]
        value = ["Ace","two","three","four","five","six","seven","eight","nine","ten","Jack","Queen","King"]

#declares the choice variable gives and populates with the users choice of coin or card
        choice = input("Do you want to toss a coin or choose a card? Choose card or coin").casefold()#validates the input to allow any case

#condition that determines whether the user has sected the coin.

        if choice == "coin":
            coin = random.randint(1,2)#Randomly selects 1 or 2
            #Prints heads or tails depending on what random number was assigned to the variable "coin"
            if coin == 1:
                print("Heads")#if the random number is 1 then displays "Heads"
            else:
                print ("Tails")#Otherwise displays "Tails"

#if the user choses card concatenates and prints an item from the value list and an item from the suit list
        elif choice =="card":
            print("You have chosen the",random.choice(value),"of",random.choice(suit))
        else:
            print("You must select choose 'card' or 'coin'")

    elif menu == "n":
            break #this ends the program if the user chooses "n"
    else:
        print("You must enter Y or N")#displays a guidance message if the user has entered something other than "Y" or "N"
