def read_puzzle_input(puzzle_input: str) -> str:
    with open(puzzle_input, 'r') as f:
        data = f.read()
    return data


data = read_puzzle_input('puzzle_input.txt')

STARTOFPACKET = 4
STARTOFMSG = 14

MarkerEndPos = int

def marker_lookup(marker_length: int) -> MarkerEndPos:
    for i in range(marker_length - 1, len(data)):
        window = data[i:i+marker_length]
        if len(set(window)) == marker_length:
            return  i + marker_length

# solution 1
print("Solution 1: ", marker_lookup(STARTOFPACKET))
# solution 2
print("Solution 2: ", marker_lookup(STARTOFMSG))
