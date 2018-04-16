import csv

fileName = "database1.csv"

csvData = []

with open(fileName,"r") as myCSVfile:
    
    dataFromFile = csv.reader(myCSVfile)
    for row in dataFromFile:
        csvData.append(row)

print(csvData)
