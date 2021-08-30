import csv

reader = csv.reader(open("namesandages.csv"))

for forename,surname,age in reader:
    print (forename,surname,age)
#csv.reader(close("namesandages.csv"))
