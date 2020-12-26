from sys import stdin
from collections import defaultdict

stdin = open("input.txt", "r")

zeros_mask = 2 ** 64 - 1
ones_mask = 0
memory = defaultdict(int)

def apply_mask(val):
    return (val | ones_mask) & zeros_mask

for line in stdin:
    command, value = line.split(' = ')
    if command[1] == 'e':
        address = int(command.split('[')[1][:-1])
        value = apply_mask(int(value))
        memory[address] = value
    else:
        zeros_mask = 2 ** 64 - 1
        ones_mask = 0
        for idx, ch in enumerate(value[::-1].strip()):
            if ch == '0':
                zeros_mask &= (2 ** 64 - 1) - 2 ** idx
            elif ch == '1':
                ones_mask |= 2 ** idx

print(memory.values())
print(sum(memory.values()))
