import csv

fileName = "database1.csv"

with open(fileName,"r") as myCSVfile:
    dataFromFile = csv.reader(myCSVfile)
    for row in dataFromFile:
        print(row)
