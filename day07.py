import csv

with open('test.csv', mode='r') as file:
    inputFile = csv.reader(file)

    for lines in inputFile:
        print(lines[0])