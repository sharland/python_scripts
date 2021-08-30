#encrypt
sentence = input('enter sentence...')
encrypted = ''
for i in range(0,len(sentence),2):
    encrypted = encrypted + sentence[i+1] + sentence[i]
    if len(sentence)% 2 == 1:
        encrypted = encrypted + sentence[i]
print(encrypted)

#decrypt
sentence = encrypted
encrypted = ''
for i in range(0,len(sentence),2):
    encrypted = encrypted + sentence[i+1] + sentence[i]
    if len(sentence)% 2 == 1:
        encrypted = encrypted + sentence[i]
print(encrypted)
