import csv

with open('input03.csv', mode='r') as file:

    inputFile = csv.reader(file)

    sum1 = 0

    for lines in inputFile:
        backpack = lines[0]
        half = int(len(backpack)/2)
        compartment1 = backpack[0:half]
        compartment2 = backpack[half:]

        for x in range(len(compartment1)):
            index = compartment1.find(compartment2[x])
            if index != -1:
                if compartment1[index].isupper():
                    ascii_index = 38
                else:
                    ascii_index = 96

                prio_value = ord(compartment1[index])-ascii_index
                break

        sum1 += prio_value

print(sum1)

with open('input03.csv', mode='r') as file:

    inputFile = csv.reader(file)

    c = 0
    group = []
    sum2 = 0


    for lines in inputFile:
        group += (lines)
        c += 1
        if c == 3:
            badge =''
            for i in group[0]:
                if i in group[1] and i in group[2]:
                    badge = i

            if badge.isupper():
                ascii_index = 38
            else:
                ascii_index = 96
            sum2 += ord(badge) - ascii_index
            group = []
            c = 0

    print(sum2)

