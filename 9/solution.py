from typing import List


def read_puzzle_input(puzzle_input: str) -> List[str]:
    with open(puzzle_input, 'r') as f:
        data = f.read().splitlines()
    return data


data = read_puzzle_input('puzzle_input.txt')

directions = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}


class Rope:
    def __init__(self):
        self.x, self.y = (0, 0)
        self.tx, self.ty = (0, 0)
        self.tail_pos = [(0, 0)]

    def move_head(self, dir: str, steps: int):
        for _ in range(steps):
            dir_x, dir_y = directions[dir]
            self.x += dir_x
            self.y += dir_y
            self.move_tail(dir)

    def move_tail(self, last_direction: str):
        if abs(self.x - self.tx) > 1 or abs(self.y - self.ty) > 1:
            self.tx, self.ty = self.x, self.y
            dir_x, dir_y = (z * -1 for z in directions[last_direction])
            self.tx += dir_x
            self.ty += dir_y
            self.tail_pos.append((self.tx, self.ty))


rope = Rope()

for line in data:
    dir, steps = line.split()
    rope.move_head(dir, int(steps))


# solution 1
print("Solution 1: ", len(set(rope.tail_pos)))
