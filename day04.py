import csv

with open('input04.csv', mode='r') as file:
    inputFile = csv.reader(file)

    total_ovelapping = 0
    for lines in inputFile:
        elf1 = lines[0]
        elf2 = lines[1]

        elf1_start = elf1.split('-')[0]
        elf1_stop = elf1.split('-')[1]

        elf2_start = elf2.split('-')[0]
        elf2_stop = elf2.split('-')[1]

        # Make sure the longest line is on top
        if (abs(int(elf1_start) - int(elf1_stop))) <= (abs(int(elf2_start) - int(elf2_stop))):
            elf1_start, elf2_start = elf2_start, elf1_start
            elf1_stop, elf2_stop = elf2_stop, elf1_stop

        print(elf1_start, elf1_stop, elf2_start, elf2_stop, elf2_start >= elf1_start and elf2_stop <= elf1_stop)

        # Is the lowest line inside the top line?
        if (elf2_start >= elf1_start) and (elf2_stop <= elf1_stop):
            total_ovelapping += 1

    print(total_ovelapping)
