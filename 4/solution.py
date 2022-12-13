from typing import List

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.read().splitlines()
    return data

data = read_puzzle_input('puzzle_input.txt')

count = 0
for line in data:
    x_range, y_range = line.split(',')
    xl, xr = (int(z) for z in x_range.split('-'))
    yl, yr = (int(z) for z in y_range.split('-'))
    x = list(range(xl, xr + 1))
    y = list(range(yl, yr + 1))
    len_x = len(x)

    x.extend(y)
    full_coverage = len(set(x))
    if len_x == full_coverage or len(y) == full_coverage:
        count += 1

# solution 1
print("Solution 1: ", count)
