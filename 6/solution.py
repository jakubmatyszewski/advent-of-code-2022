def read_puzzle_input(puzzle_input: str) -> str:
    with open(puzzle_input, 'r') as f:
        data = f.read()
    return data


data = read_puzzle_input('puzzle_input.txt')

window_len = 4
for i in range(window_len - 1, len(data)):
    window = data[i:i+window_len]
    if len(set(window)) == window_len:
        # solution 1
        print("Solution 1: ", i + window_len)
        break
