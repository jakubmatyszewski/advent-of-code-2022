from typing import List

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.readlines()
    return data

data = read_puzzle_input('puzzle_input.txt')
# Rock = 0, Paper = 1, Scissors = 2
shapes = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}

score = 0

for line in data:
    opponent, me = (shapes[x] for x in line.split())
    round_outcome = opponent - me
    if round_outcome % 3 == 2:
        score += 6 + me + 1
    elif not round_outcome:
        score += 3 + me + 1
    else:
        score += me + 1
    
# solution 1
print("Solution 1: ", score)

score = 0
for line in data:
    shapes['X'] = -1 # 0
    shapes['Y'] = 0 # 3
    shapes['Z'] =  1 # 6
    opponent, round_outcome = (shapes[x] for x in line.split())
    me = (round_outcome + opponent) % 3
    score += me + 1 + 3 + 3 * round_outcome

# solution 2
print("Solution 2: ", score)
