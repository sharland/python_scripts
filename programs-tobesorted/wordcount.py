def countwords(sentence):

    wordcount = 0

    
    for i in range(0,len(sentence)):
        if sentence[i] == ' ':
            wordcount += 1

    wordcount += 1
    print('no of words = ', wordcount)
    return

def countvowels(sentence):

    vowelcount = 0               
    for i in range(0,len(sentence)):
        if sentence[i]in ['a','A','e','E','i','I','o','O','u','U']:
            vowelcount = vowelcount + 1

    print('no of vowels = ', vowelcount)
    return

s = input('enter sentence...')
countwords(s)
countvowels(s)
                
