from collections import deque
from typing import List, Union

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.read().splitlines()
    return data

data = read_puzzle_input('puzzle_input.txt')


def solve(start: Union[str, list]) -> int:
    Q = deque((i, j, 0, 'a') for i in range(len(data))
                             for j in range(len(data[i]))
                             if data[i][j] in start)

    visited = set((i, j) for i, j, _, _ in Q)

    while len(Q):
        i, j, d, a = Q.popleft()
        if data[i][j] == 'E': return d
        for ni, nj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if (
                len(data) > ni >= 0
                and len(data[ni]) > nj >= 0
                and (ni,nj) not in visited
               ):
                b = data[ni][nj].replace('E', 'z')
                if ord(a) + 1 >= ord(b):
                    visited.add((ni,nj))
                    Q.append((ni, nj, d+1, b))


# solution 1
print("Solution 1: ", solve('S'))

# solution 2
print("Solution 2: ", solve(['S', 'a']))
