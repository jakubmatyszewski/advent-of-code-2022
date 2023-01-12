import functools
import re
from typing import List

def read_puzzle_input(puzzle_input: str) -> List[str]: 
    with open(puzzle_input, 'r') as f:
        data = f.read().splitlines()
    return data

data = read_puzzle_input('puzzle_input.txt')


def parse_instructions(data: list) -> list:
    i = 0
    monkees = []
    for line in data:
        line = line.lower().strip()
        if not line: continue

        if line.startswith('monkey'):
            monkees.append({'items': [], 'operation': [], 'test': 1, 'true': 0, 'false': 0, 'busy': 0})
            i += 1

        instruction = re.findall(r'(\w+):', line)[0]
        match instruction:
            case 'items':
                monkees[i-1]['items'].extend([int(x) for x in re.findall(r'\d+', line)])
            case 'operation':
                operation = line.split('=')[1].strip()

                if '+' in operation:
                    op_type = ["add"]
                    values = [int(x) if x.isnumeric() else x for x in operation.split(' + ')]
                elif '*' in operation:
                    op_type = ["mul"]
                    values = [int(x) if x.isnumeric() else x for x in operation.split(' * ')]
                monkees[i-1]['operation'].extend(op_type + values)
            case 'test':
                monkees[i-1]['test'] = int(re.search(r'\d+', line).group(0))
            case 'true':
                monkees[i-1]['true'] = int(re.search(r'\d+', line).group(0))
            case 'false':
                monkees[i-1]['false'] = int(re.search(r'\d+', line).group(0))
    return monkees

def test_item(worry: int, test: int) -> bool:
    if not worry % test:
        return True
    return False

def monkee_inspect(worry: int, operation: str, values: List[int|str]) -> int:
    values = [val if isinstance(val, int) else worry for val in values]
    
    if operation == 'add':
        return sum(values)
    elif operation == 'mul':
        return functools.reduce(lambda x, y: x * y, values)

def play_round(monkees: list) -> None:
    modulo = functools.reduce(lambda x, y: x*y, [monkee['test'] for monkee in monkees])
    for monkee in monkees:
        for item in monkee['items']:
            monkee["busy"] += 1
            operation = monkee['operation'][0]
            values = monkee['operation'][1:]
            # new = monkee_inspect(item, operation, values)//3
            new = monkee_inspect(item, operation, values) % modulo

            test_outcome = test_item(new, monkee['test'])
            if test_outcome:
                monkees[monkee['true']]["items"].append(new)
            else:
                monkees[monkee['false']]["items"].append(new)
        monkee['items'] = []

monkees = parse_instructions(data)

# for _ in range(20):
#     play_round(monkees)

# # solution 1
# print("Solution 1: ", functools.reduce(lambda x, y: x * y, sorted([monkee['busy'] for monkee in monkees], reverse=True)[:2]))

for i in range(10000):
    play_round(monkees)

# solution 2
print("Solution 2: ", functools.reduce(lambda x, y: x * y, sorted([monkee['busy'] for monkee in monkees], reverse=True)[:2]))
