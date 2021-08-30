#this program is to allow the user to guess a word
print ('The new word?')
NewWord = input()
print('Your guess?')
UserWordGuess = input()     
if UserWordGuess == NewWord:
    print('CORRECT')
else:
    print('INCORRECT')

