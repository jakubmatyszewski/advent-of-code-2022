import re
from typing import List

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.read()
    return data

data = read_puzzle_input('puzzle_input.txt')

crates, manual = [x.splitlines() for x in data.split('\n\n')]

def parse_crates(crates: List[str]):
    stacks = {k: [] for k in range(1, 10)}
    for line in crates[:len(crates) - 1]:
        for i in range(9):
            crate = line[1 + 4 * i].strip()
            if crate:
                stacks[i + 1].append(crate)

    for v in stacks.values():
        v.reverse()
    return stacks

stacks = parse_crates(crates)
for line in manual:
    move, src, dest = tuple(map(int, re.findall(r'\d+', line)))
    pop = reversed(stacks[src][len(stacks[src]) - move:])
    stacks[src] = stacks[src][:len(stacks[src]) - move]
    stacks[dest].extend(pop)

# solution 1
print("Solution 1: ", ''.join([stacks[k][-1] for k in stacks.keys()]))

stacks = parse_crates(crates)
for line in manual:
    move, src, dest = tuple(map(int, re.findall(r'\d+', line)))
    pop = stacks[src][len(stacks[src]) - move:]
    stacks[src] = stacks[src][:len(stacks[src]) - move]
    stacks[dest].extend(pop)

# solution 2
print("Solution 2: ", ''.join([stacks[k][-1] for k in stacks.keys()]))
