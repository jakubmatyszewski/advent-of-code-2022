from typing import List

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.readlines()
    return data

data = read_puzzle_input('puzzle_input.txt')
# Rock = 1, Paper = 2, Scissors = 3
shapes = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

score = 0

for line in data:
    opponent, me = (shapes[x] for x in line.split())
    round_outcome = opponent - me
    if round_outcome % 3 == 2:
        score += 6 + me
    elif not round_outcome:
        score += 3 + me
    else:
        score += me
    
# solution 1
print("Solution 1: ", score)
