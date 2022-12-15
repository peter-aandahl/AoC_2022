import csv

with open('test07.csv', mode='r') as file:
    inputFile = csv.reader(file)

    for lines in inputFile:
        line = lines[0]

        if (line[0]=='$'):
            print('Command detected')

        if (line[0:3]=='dir'):
            print('Directory found')

        if (line[0] in '0123456789'):
            print('File detected')

