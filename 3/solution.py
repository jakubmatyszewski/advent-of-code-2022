from typing import List

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.read().splitlines()
    return data

def compute_priority(char: str) -> int:
    priority = ord(char.lower()) - 96 # ord(a) = 97; thus - 96 so a = 1
    if char.isupper():
        # compensate for uppercase letters
        priority += 26
    
    return priority

data = read_puzzle_input('puzzle_input.txt')

score = 0
for line in data:
    half = int(len(line)/2)
    duplicate = set(line[half:]).intersection(set(line[:half])).pop()
    
    score += compute_priority(duplicate)

# solution 1
print("Solution 1: ", score)

score = 0
for i in range(int(len(data)/3)):
    bags_of_3 = data[3*i:3*(i+1)]
    badge = set(bags_of_3[0]).intersection(set(bags_of_3[1])).intersection(set(bags_of_3[2])).pop()
    score += compute_priority(badge)

# solution 2
print("Solution 2: ", score)
