import csv

with open('input05.csv', mode='r') as file:
    inputFile = csv.reader(file)

    width = 9
    height = 8
    fixed_height = height

    board = []
    new_board =[]

    stack= []
    row = []

    row_width = 4 * width - 1

    for lines in inputFile:

            row = lines[0].ljust(row_width,' ')

            for c in range(1, row_width,4):
                stack.append(row[c])

            board.append(stack)
            stack = []

            if height == 0:
                break
            else:
                height -= 1

    new_row=[]

    for y in range(0, fixed_height+1):
        for x in range(0, width):
            if board[x][y] != ' ':
                new_row.append(board[x][y])

        # Drop the index if needed
        if new_row[-1] in '123456789':
            new_row.pop()
        # Reverse the row
        new_board.append(new_row[::-1])
        new_row = []

    #Now that we have the board we can parse the moves

    for lines in inputFile:
        if lines:
            amount = int(lines[0].split(' ')[1])
            start = int(lines[0].split(' ')[3])
            end = int(lines[0].split(' ')[5])

            moving_stack =[]
            for a in range(0,amount):
                block = new_board[start-1].pop()
                moving_stack.append(block)

            #Reverse the stack
            moving_stack = moving_stack[::-1]

            for b in moving_stack:
                new_board[end-1].append(b)


    for b in new_board:
        print(b[-1], end='')


