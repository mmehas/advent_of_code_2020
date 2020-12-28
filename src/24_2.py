from collections import defaultdict
from sys import stdin

stdin = open("input.txt", "r")

moves = [('e', 1, 0), ('w', -1, 0), ('nw', 0, 1), ('ne', 1, 1), ('sw', -1, -1), ('se', 0, -1)]
black = set()

for line in stdin:
    line = line.strip()
    idx = 0
    x, y = 0, 0
    while idx < len(line):
        for move, dx, dy in moves:
            if line[idx:].startswith(move):
                x, y = x + dx, y + dy
                idx += len(move)
                break
    if (x, y) in black:
        black.remove((x, y))
    else:
        black.add((x, y))

for _ in range(100):
    near = defaultdict(int)
    for x, y in black:
        if (x, y) not in near:
            near[(x, y)] = 0
        for _, dx, dy in moves:
            tx, ty = x + dx, y + dy
            near[(tx, ty)] += 1

    for coords, n in near.items():
        x, y = coords
        if (x, y) in black and (n != 1 and n != 2):
            black.remove((x, y))
        elif ((x, y) not in black) and n == 2:
            black.add((x, y))

print(len(black))
