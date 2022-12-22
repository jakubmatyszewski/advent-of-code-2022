from typing import List


def read_puzzle_input(puzzle_input: str) -> List[str]:
    with open(puzzle_input, 'r') as f:
        data = f.read().splitlines()
    return data

data = read_puzzle_input('puzzle_input.txt')

dim = len(data[0])
visible = dim * 2 + (dim - 2) * 2

def transpone_table(data):
    data_t = [[] for _ in range(len(data[0]))]
    for line in data:
        for i, x in enumerate(line):
            data_t[i].append(x)
    return data_t

data_t = transpone_table(data)

for i, line in enumerate(data[1:dim-1], 1):
    for j, num in enumerate(line[1:dim-1], 1):
        if(num > max(line[:j]) or
           num > max(line[j+1:]) or
           num > max(data_t[j][:i]) or
           num > max(data_t[j][i+1:])):
           visible += 1

# solution 1
print("Solution 1: ", visible)

def scenic_score(height, side):
    side_score = [1 if height > x else 0 for x in side]
    
    try:
        r = side_score.index(0) + 1
    except ValueError:
        r = len(side)

    return r

top_scenic_score = 0
for i, line in enumerate(data[1:dim-1], 1):
    for j, num in enumerate(line[1:dim-1], 1):
        left = scenic_score(num, list(reversed(line[:j])))
        right = scenic_score(num, line[j+1:])
        up = scenic_score(num, list(reversed(data_t[j][:i])))
        down = scenic_score(num, data_t[j][i+1:])
        score = left * right * up * down

        (top_scenic_score := max(score, top_scenic_score))

# solution 2
print("Solution 2: ", top_scenic_score)
