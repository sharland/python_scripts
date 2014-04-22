#! /usr/local/bin/python3
#Credit Laura @codeboom source http://codeboom.wordpress.com/sweet-resources/hangman/

# Blackjack program (21)
import random

# Functions
# ----------

# Deals one card to the player
def deal_card():
    return random.randrange(1,10)

# Only performed at the start when we deal 2 cards 
def starting_deal():
    return deal_card() + deal_card()

# Compare scores to check who has won
def check_win(playerScore,dealerScore):
    print "Your total is ",playerScore
    print "Dealer's total is ",dealerScore
    if playerScore > dealerScore:
        print "You win"
    elif playerScore == dealerScore:
        print "Push. Nobody wins"
    else:
        print "Dealer wins"

# Check whether a score is bust
def is_bust(score):
    if score > 21:
        return True
    else:
        return False

# Decide whether the dealer is going to draw
def dealer_draw(dealerScore):
    if dealerScore == 17:
            dealer = dealer_draw(dealer)

            # Check if this causes the dealer to bust
            if is_bust(dealer):
                print "Dealer has bust! You win"
                endGame = True