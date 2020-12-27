import numpy as np

from sys import stdin, stdout
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

    return a

tiles = []
while (tile := read_tile()) is not None:
    tiles.append(tile)

def apply_config(grid, config):
    rot, flip = config // 2, config % 2
    grid = np.rot90(grid, k=rot)
    if flip:
        grid = np.flip(grid, axis=0)
    return grid

def prepare(sol):
    tile_id, config = sol
    grid = tiles[tile_id]
    return apply_config(grid, config)

def print_grid(out_grid, x, y, grid):
    out_grid[x: x + tile_w - 2, y: y + tile_w - 2] = np.flip(grid[1:-1, 1:-1], axis=0)

solution = [[[88, 5], [95, 2], [37, 7], [12, 6], [119, 6], [78, 7], [21, 1], [8, 5], [138, 6], [14, 7], [71, 6], [127, 1]], [[9, 6], [126, 7], [114, 2], [93, 7], [40, 1], [107, 4], [3, 4], [124, 4], [31, 5], [76, 1], [20, 1], [46, 4]], [[103, 0], [26, 4], [24, 5], [52, 2], [58, 6], [29, 2], [133, 4], [39, 7], [64, 1], [57, 2], [45, 2], [73, 1]], [[1, 6], [10, 2], [99, 1], [35, 5], [94, 6], [81, 2], [139, 4], [118, 7], [111, 6], [109, 5], [141, 6], [44, 2]], [[108, 4], [121, 1], [70, 6], [134, 0], [50, 7], [34, 5], [112, 2], [84, 1], [98, 0], [100, 7], [79, 5], [22, 5]], [[120, 7], [96, 6], [69, 1], [27, 0], [15, 1], [4, 5], [62, 6], [85, 5], [49, 1], [68, 0], [101, 7], [104, 4]], [[18, 6], [106, 5], [0, 7], [17, 7], [110, 6], [38, 2], [56, 0], [143, 5], [117, 1], [6, 4], [13, 6], [77, 5]], [[90, 4], [7, 2], [123, 5], [131, 7], [132, 6], [30, 4], [51, 7], [116, 1], [36, 1], [11, 1], [5, 5], [140, 4]], [[53, 4], [92, 5], [130, 1], [122, 0], [129, 1], [66, 6], [60, 6], [89, 6], [48, 5], [25, 6], [28, 4], [97, 7]], [[113, 1], [61, 2], [67, 0], [115, 2], [83, 2], [125, 1], [87, 0], [23, 1], [82, 0], [47, 6], [55, 5], [128, 7]], [[41, 6], [2, 5], [42, 0], [80, 0], [33, 7], [137, 6], [63, 2], [32, 1], [54, 2], [75, 2], [135, 6], [65, 4]], [[105, 2], [59, 2], [136, 5], [16, 1], [74, 2], [72, 7], [86, 0], [43, 7], [102, 7], [91, 0], [19, 5], [142, 2]]]
#solution = [[[2, 1], [4, 5], [6, 5]], [[5, 7], [3, 5], [7, 5]], [[8, 4], [0, 5], [1, 5]]]

pattern = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ']

pattern = np.array([[ch == '#' for ch in line] for line in pattern])

output_grid = np.zeros(((tile_w - 2) * len(solution), (tile_w - 2) * len(solution)), dtype=np.bool)

x, y = 0, 0
for idx in range(len(solution)):
    y = 0
    for idy in range(len(solution[0])):
        print_grid(output_grid, x, y, prepare(solution[idx][idy]))
        y += tile_w - 2
    x += tile_w - 2

def display_grid(grid):
    for x in range(len(grid)):
        if x % (tile_w - 2) == 0 and x != 0:
            stdout.write('\n')
        for y in range(len(grid[0])):
            if y % (tile_w - 2) == 0 and y != 0:
                stdout.write(' ')
            if grid[x][y]:
                stdout.write('#')
            else:
                stdout.write('.')
        stdout.write('\n')

def find_pattern(grid, pattern):
    w, h = grid.shape
    pw, ph = pattern.shape
    res = 0
    for x in range(w - pw + 1):
        for y in range(h - ph + 1):
            if (pattern & grid[x: x + pw, y: y + ph]).sum() == pattern.sum():
                res += 1
    return res

print(output_grid.sum())
for config in range(8):
    rotated_grid = apply_config(output_grid, config)
    res = output_grid.sum() - find_pattern(rotated_grid, pattern) * pattern.sum()
    print(res)