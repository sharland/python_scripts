# File: csvreadfile.py

import csv

reader = csv.reader(open("csvfile.txt"))

for name, score in reader:
    print (name, score)
#reader.close()


