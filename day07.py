import csv
from collections import defaultdict
from pathlib import Path

with open('input07.csv', mode='r') as file:
    inputFile = csv.reader(file)

    current_dir = Path('/')
    catalog_sizes = defaultdict(int)

    for lines in inputFile:
        if lines[0].startswith('$ cd'):
            current_dir = (current_dir / lines[0][5:]).resolve()

        elif lines[0].startswith('$ ls'):
            continue

        elif lines[0].startswith('dir'):
            continue

        else:
            size = int(lines[0].split(' ')[0])
            catalog_sizes[current_dir] += size

            for parent in current_dir.parents:
                catalog_sizes[parent] += size


    free_space = catalog_sizes[Path('C:/')]
    required = 30000000 - (70000000 - free_space)


    print('Part 1')
    print(sum(value for value in catalog_sizes.values() if value <= 100000))
    print('Part 2')
    print(min(value for value in catalog_sizes.values() if value >= required))

