import numpy as np

from sys import stdin, stdout
from tqdm import tqdm

stdin = open("input.txt", "r")
tile_w = 10

def read_tile():
    try:
        s = stdin.readline().strip()
        num = int(s[5:-1])
    except:
        return None
    a = np.zeros((tile_w, tile_w), dtype=np.bool)
    cnt = 0
    while (line := stdin.readline().strip()) != '':
        for idx, ch in enumerate(line):
            a[tile_w - cnt - 1, idx] = ch == '#'
        cnt += 1

    return [num, a]

def vertical_compatibility(tile1, config1, tile2, config2):
    rot1, flip1 = config1 // 2, config1 % 2
    rot2, flip2 = config2 // 2, config2 % 2
    tile1 = np.rot90(tile1, k=rot1)
    if flip1:
        tile1 = np.flip(tile1, axis=0)
    tile2 = np.rot90(tile2, k=rot2)
    if flip2:
        tile2 = np.flip(tile2, axis=0)
    return all(tile1[-1] == tile2[0])

def horizontal_compatibility(tile1, config1, tile2, config2):
    rot1, flip1 = config1 // 2, config1 % 2
    rot2, flip2 = config2 // 2, config2 % 2
    tile1 = np.rot90(tile1, k=rot1)
    if flip1:
        tile1 = np.flip(tile1, axis=0)
    tile2 = np.rot90(tile2, k=rot2)
    if flip2:
        tile2 = np.flip(tile2, axis=0)
    return all(tile1[:,-1] == tile2[:, 0])

def vertical_ok(idx1, config1, idx2, config2):
    return vert_compatible[idx1, config1, idx2, config2]

def horizontal_ok(idx1, config1, idx2, config2):
    return hor_compatible[idx1, config1, idx2, config2]

tiles = []
while (tile := read_tile()) != None:
    tiles.append(tile)

vert_compatible = np.zeros((len(tiles), 8, len(tiles), 8), dtype=np.bool)
hor_compatible = np.zeros((len(tiles), 8, len(tiles), 8), dtype=np.bool)
for idx1, tile1 in tqdm(enumerate(tiles)):
    for idx2, tile2 in enumerate(tiles):
        for config1 in range(8):
            for config2 in range(8):
                vert_compatible[idx1, config1, idx2, config2] = vertical_compatibility(tile1[1], config1, tile2[1], config2)
                hor_compatible[idx1, config1, idx2, config2] = horizontal_compatibility(tile1[1], config1, tile2[1], config2)

grid_w = int(len(tiles) ** (0.5) + 1e-10)
grid = [[None for _ in range(grid_w)] for _ in range(grid_w)]

def valid_grid(grid, tiles, cur, w, left):
    if cur == w * w:
        yield grid
    else:
        x, y = cur // w, cur % w
        for idx in left:
            for config in range(8):
                valid = True
                valid &= horizontal_ok(*grid[x][y-1], idx, config) if y != 0 else True
                valid &= vertical_ok(idx, config, *grid[x-1][y]) if x != 0 else True
                if valid:
                    grid[x][y] = [idx, config]
                    left.remove(idx)
                    yield from valid_grid(grid, tiles, cur + 1, w, left)
                    left.add(idx)

sol = next(valid_grid(grid, tiles, 0, grid_w, set(range(0, len(tiles)))))
print(sol)
print(np.prod([tiles[id][0] for id in [sol[0][0][0], sol[grid_w-1][0][0], sol[grid_w-1][grid_w-1][0], sol[0][grid_w-1][0]]]))