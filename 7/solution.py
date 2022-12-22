from collections import defaultdict

def read_puzzle_input(puzzle_input: str) -> str:
    with open(puzzle_input, 'r') as f:
        data = f.read().splitlines()
    return data


data = read_puzzle_input('puzzle_input.txt')

sizes = defaultdict(int)
path = []
for line in data:
    if line.startswith("$ cd"):
        d = line.split()[2]
        if d == "/":
            path.append("/")
        elif d == "..":
            last = path.pop()
        else:
            path.append(f"{path[-1]}{'/' if path[-1] != '/' else ''}{d}")
    if line[0].isnumeric():
        for p in path:
            sizes[p] += int(line.split()[0])


# solution 1
print("Solution 1: ", sum(s for s in sizes.values() if s <= 100_000))

# solution 2
print("Solution 2: ", min(s for s in sizes.values() if (70000000 - sizes["/"] + s) >= 30000000))
