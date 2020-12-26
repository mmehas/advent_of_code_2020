from sys import stdin

import numpy as np

stdin = open("input.txt", "r")
a = stdin.readlines()

def check_slope(a, slope):
    dx, dy = slope
    x, y = 0, 0
    n = len(a)
    w = len(a[0]) - 1
    res = 0
    while x < n:
        res += a[x][y] == '#'
        x += dx
        y = (y + dy) % w

    return res

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
print(np.prod([check_slope(a, slope) for slope in slopes]))