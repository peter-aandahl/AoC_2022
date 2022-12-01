import csv

with open('input01.csv', mode='r') as file:

    inputFile = csv.reader(file)

    elves = []
    total = 0

    for lines in inputFile:
        #For each Elf
        if lines:
            total = total + int(lines[0])
        else:
            elves.append(total)
            total = 0

    elves.sort()
    print(elves[-1:][0])
    print(sum(elves[-3:]))
