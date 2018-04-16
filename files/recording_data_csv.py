f = open('database1.csv','a')

contLoop = True

while contLoop == True:
    newGame = input("Enter game name: ")
    newGenre = input("Enter genre: ")
    newReleaseDate = int(input("Enter year of release: "))

    record = "{0},{1},{2}".format(newGame,newGenre,newReleaseDate)+"\n"
    f.write(record)
    loop = input("Do you want to continue?: ")
    if loop == "N" or loop == "n":
        contLoop = False
    else:
        continue

f.close()
