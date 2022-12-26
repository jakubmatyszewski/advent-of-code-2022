from typing import List

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.read().splitlines()
    return data

data = read_puzzle_input('puzzle_input.txt')

REGISTER = [20, 60, 100, 140, 180, 220]


class Computer:
    def __init__(self, data):
        self.cycle = 0
        self.x = 1
        self.output = 0
        self.data = data
        self.crt = [['.'] * 40 for _ in range(6)]
        

    def update_cycle(self):
        self.cycle += 1
        self.gpu()
        if self.cycle in REGISTER:
            self.output += self.cycle * self.x

    def run(self):
        for line in self.data:
            if line.startswith('noop'):
                self.update_cycle()
            else:
                addx = int(line.split()[1])
                self.update_cycle()
                self.update_cycle()
                self.x += addx
        return self.output
    
    def gpu(self):
        column = (self.cycle - 1) % 40
        row = int((self.cycle - 1) / 40)
        sprite = [self.x -1, self.x, self.x + 1]
        if column in sprite:
            self.crt[row][column] = "#"
        else:
            self.crt[row][column] = "."

    def display(self):
        print('\n'.join([''.join(line) for line in self.crt]))

computer = Computer(data)

# solution 1
print("Solution 1: ", computer.run())

# solution 2
print("Solution 2: ", computer.display())
