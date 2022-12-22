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

# # solution 2
# print("Solution 2: ", score)
