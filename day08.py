import csv

with open('test08.csv', mode='r') as file:
    inputFile = csv.reader(file)

    row = []
    grid = []
    visible_trees = 0

    for lines in inputFile:
        for a in lines[0]:
            row.append(a)
        grid.append(row)
        row = []

    # Grid now contains all trees
    # Shape of grid:
    # print(str(len(grid[0])) + 'x' + str(len(grid)))

    # All trees on the edge are visible
    visible_trees += len(grid[0]) * 2 + len(grid) * 2 - 4

    # For each tree in the interior: if all trees in ANY of the 4 directions are lower, count it as visible.
    # x,y are coordinates of trees to be checked
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            check_tree = grid[y][x]
            # print('At Y={},X={} a tree is {}'.format(y,x,check_tree))
            t_visible = 1
            b_visible = 1
            l_visible = 1
            r_visible = 1
            for t in range(0, y):
                # print('Trees above are {}'.format(grid[t][x]))
                if grid[t][x] >= check_tree:
                    t_visible = 0
                    # print('{},{} is not visible from top'.format(y,x))

            for b in range(y + 1, len(grid)):
                # print('Trees below are {}'.format(grid[b][x]))
                if grid[b][x] >= check_tree:
                    b_visible = 0
                    # print('{},{} is not visible from bottom'.format(y,x))

            for l in range(0, x):
                # print('Trees to the left are {}'.format(grid[y][l]))
                if grid[y][l] >= check_tree:
                    l_visible = 0
                    # print('{},{} is not visible from left'.format(y,x))

            for r in range(x + 1, len(grid[0])):
                # print('Trees to the right are {}'.format(grid[y][r]))
                if grid[y][r] >= check_tree:
                    r_visible = 0
                    # print('{},{} is not visible from right'.format(y,x))

            if t_visible + b_visible + l_visible + r_visible > 0:
                visible_trees += 1

    print(visible_trees)

    # Part 2

    t_visible = 1
    b_visible = 1
    l_visible = 1
    r_visible = 1
    # This time, for each tree in the grid:
    # x,y are coordinates of trees to be checked
    for x in range(0, len(grid[0])):
        for y in range(0, len(grid)):
            check_tree = grid[y][x]
            print(check_tree)
            for b in range(y + 1, len(grid)):
                print('Trees below are {}'.format(grid[b][x]))



