#roll double sixes program
import random
turns = 0
games = 0

file = open('gameresults.txt',"w")

for i in range(201):
	
	while turns != 1:
		turns = 0
		games += 1
		carryOn = True
		while carryOn == True:
			a = random.randint(1,6)
			b = random.randint(1,6)
			c = a+b
			print(c)
			turns += 1
			if c == 12:
				carryOn = False
				print ("turns: "+str(turns))
				print("games: "+str(games))
				
	file.writelines(str(games)+"\n")