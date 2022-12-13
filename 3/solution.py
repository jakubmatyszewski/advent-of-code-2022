from typing import List

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.readlines()
    return data


data = read_puzzle_input('puzzle_input.txt')
score = 0

for line in data:
    half = int(len(line)/2)
    duplicate = set(line[half:]).intersection(set(line[:half])).pop()
    if duplicate.isupper():
        # compensate for uppercase letters
        score += 26
    
    priority = ord(duplicate.lower()) - 96 # ord(a) = 97; thus - 96 so a = 1
    score += priority

    

# solution 1
print("Solution 1: ", score)

