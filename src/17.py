from collections import defaultdict
from sys import stdin

def gen_neighborhood(coords, d):
    def gen_neighborhood_local(coords, d, idx, n_coords):
        if idx == len(coords):
            if tuple(n_coords) != coords:
                yield tuple(n_coords)
        else:
            for dx in range(-d, d + 1):
                n_coords.append(coords[idx] + dx)
                yield from gen_neighborhood_local(coords, d, idx + 1, n_coords)
                del n_coords[-1]

    yield from gen_neighborhood_local(coords, d, 0, [])

stdin = open("input.txt", "r")

a = stdin.readlines()
coords = []
for x in range(len(a)):
    for y in range(len(a[0]) - 1):
        if a[x][y] == '#':
            coords.append((x, y, 0))

active = set(coords)

for _ in range(6):
    neighbors = defaultdict(int)
    for coords in active:
        for n_coords in gen_neighborhood(coords, 1):
            neighbors[n_coords] += 1
    new_active = set()
    for coords, n_count in neighbors.items():
        if not coords in active:
            if n_count == 3:
                new_active.add(coords)
        else:
            if 2 <= n_count and n_count <= 3:
                new_active.add(coords)
    active = new_active

print(len(active))