from typing import List


def read_puzzle_input(puzzle_input: str) -> List[str]:
    with open(puzzle_input, 'r') as f:
        data = f.read().splitlines()
    return data


data = read_puzzle_input('puzzle_input.txt')

directions = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}

def move_head(dir: str, steps: int):
    for _ in range(steps):
        direction = directions[dir]
        rope[0] = [[a+c, b+d] for [a, b], [c, d] in zip([rope[0]], [direction])][0]
        move_knot(1, direction)

def move_knot(knot_id: int, direction: List = []):
    if (abs(rope[knot_id - 1][0] - rope[knot_id][0]) > 1 or  # x diff
        abs(rope[knot_id - 1][1] - rope[knot_id][1]) > 1):   # y diff

        direction = get_direction(rope[knot_id - 1], rope[knot_id])
        rope[knot_id] = [[a+c, b+d]
                    for [a, b], [c, d] in zip([rope[knot_id]], [direction])][0]
        if knot_id == rope_length - 1:
            tail_pos.append(tuple(rope[knot_id]))

        if knot_id < rope_length - 1:
            move_knot(knot_id + 1, direction)

def get_direction(head, tail):
    x, y = [[a-c, b-d]
                    for [a, b], [c, d] in zip([head], [tail])][0]
    if abs(x) == 2 and not y: # horizontal
            x = 1 if x > 0 else -1
    elif abs(y) == 2 and not x: # vertical
        y = 1 if y > 0 else -1
    elif (abs(x) == 2 and abs(y) in (1, 2)) or (abs(y) == 2 and abs(x) in (1, 2)):
        x = 1 if x > 0 else -1
        y = 1 if y > 0 else -1
    return [x, y]


rope_length = 2
rope = [[0, 0] for _ in range(rope_length)]
tail_pos = [(0, 0)]
for line in data:
    dir, steps = line.split()
    move_head(dir, int(steps))



# solution 1
print("Solution 1: ", len(set(tail_pos)))

rope_length = 10
rope = [[0, 0] for _ in range(rope_length)]
tail_pos = [(0, 0)]
for line in data:
    dir, steps = line.split()
    move_head(dir, int(steps))

# solution 2
print("Solution 2: ", len(set(tail_pos)))
