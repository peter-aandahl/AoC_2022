import csv

with open('input06.csv', mode='r') as file:
    inputFile = csv.reader(file)

    for lines in inputFile:
        signal = lines[0]
x1 =''
c = 0
for x in signal:
    x1 += x
    c += 1
    if c >= 4:
        s = 0
        for y in range(c-1,c-5,-1):
            s += x1[c - 4:c].count(x1[y])
        if s == 4:
            print('Signal detected at {}'.format(c))
            break

x1 =''
c = 0
for x in signal:
    x1 += x
    c += 1
    if c >= 14:
        s = 0
        for y in range(c-1,c-15,-1):
            s += x1[c - 14:c].count(x1[y])
        if s == 14:
            print('Message detected at {}'.format(c))
            break