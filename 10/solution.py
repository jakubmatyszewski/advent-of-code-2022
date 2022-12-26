from typing import List

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.read().splitlines()
    return data

data = read_puzzle_input('puzzle_input.txt')

REGISTER = [20, 60, 100, 140, 180, 220]

class CPU:
    def __init__(self, data):
        self.cycle = 0
        self.x = 1
        self.output = 0
        self.data = data

    def update_cycle(self):
        self.cycle += 1
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

computer = CPU(data)

# solution 1
print("Solution 1: ", computer.run())
