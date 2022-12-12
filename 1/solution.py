from typing import List

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.readlines()
    return data

class ElvesHQ:
    def __init__(self, data: List[str]):
        self.elves = []
        self.data = data

    def compute_elves_calories(self) -> None:
        current_cal = 0

        for line in self.data:
            if line == '\n':
                self.elves.append(current_cal)
                current_cal = 0
                continue
            current_cal += int(line.strip())


    def find_max_calories(self) -> int:
        most_calories = max(self.elves)
        return most_calories

    def find_3_best_backups(self) -> int:
        self.elves.sort()
        return sum(self.elves[::-1][0:3])

data = read_puzzle_input('puzzle_input.txt')
hq = ElvesHQ(data)
hq.compute_elves_calories()

# solution 1
print("Solution 1: ", hq.find_max_calories())

# solution 2
print("Solution 2: ", hq.find_3_best_backups())

