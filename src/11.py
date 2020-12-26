from sys import stdin
stdin = open("input.txt", "r")

a = [list(l.strip()) for l in stdin.readlines()]
h, w = len(a), len(a[0])

def occupied(a, x, y):
    res = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if x + dx >= 0 and x + dx < h and y + dy >= 0 and y + dy < w and (dx != 0 or dy != 0):
                res += a[x + dx][y + dy] == '#'
    return res

def update(a):
    out = [None] * h
    for idx in range(h):
        out[idx] = ['.'] * w
    for x in range(h):
        for y in range(w):
            if a[x][y] == 'L' and occupied(a, x, y) == 0:
                out[x][y] = '#'
            elif a[x][y] == '#' and occupied(a, x, y) >= 4:
                out[x][y] = 'L'
            else:
                out[x][y] = a[x][y]
    return out

def print_field(a):
    for l in a:
        print(''.join(l))

    print('\n')

while True:
    print_field(a)
    out = update(a)
    if out == a:
        res = sum([l.count('#') for l in a])
        print(res)
        exit()
    a = out