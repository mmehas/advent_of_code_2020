from sys import stdin
from collections import defaultdict

stdin = open("input.txt", "r")

memory = defaultdict(int)

def apply_mask(val):
    return val | ones_mask

def set_bit(val, idx, bit):
    if bit == 1:
        val |= 2 ** idx
    else:
        val &= 2 ** 64 - 1 - 2 ** idx
    return val

def gen_floating(base_address, idx, cur_address, floating):
    if len(floating) == 0 or idx > floating[-1]:
        yield cur_address
    else:
        if idx in floating:
            yield from gen_floating(base_address, idx + 1, set_bit(cur_address, idx, 0), floating)
            yield from gen_floating(base_address, idx + 1, set_bit(cur_address, idx, 1), floating)
        else:
            yield from gen_floating(base_address, idx + 1, cur_address, floating)

for line in stdin:
    command, value = line.split(' = ')
    if command[1] == 'e':
        address = int(command.split('[')[1][:-1])
        value = int(value)
        address = apply_mask(address)
        for cur_address in gen_floating(address, 0, address, floating):
            memory[cur_address] = value
    else:
        ones_mask = 0
        floating = []
        for idx, ch in enumerate(value[::-1].strip()):
            if ch == 'X':
                floating.append(idx)
            elif ch == '1':
                ones_mask |= 2 ** idx

print(sum(memory.values()))
