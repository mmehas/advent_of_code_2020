from sys import stdin
stdin = open("input.txt", "r")

a = [list(l.strip()) for l in stdin.readlines()]
h, w = len(a), len(a[0])

def occupied(a, x, y):
    res = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for k in range(1, max(w, h) + 1):
                if x + dx * k >= 0 and x + dx * k < h and y + dy * k >= 0 and y + dy * k < w and (dx != 0 or dy != 0):
                    val = a[x + dx * k][y + dy * k]
                    if val == 'L':
                        break
                    if val == '#':
                        res += 1
                        break
    return res

def update(a):
    out = [None] * h
    for idx in range(h):
        out[idx] = ['.'] * w
    for x in range(h):
        for y in range(w):
            if a[x][y] == 'L' and occupied(a, x, y) == 0:
                out[x][y] = '#'
            elif a[x][y] == '#' and occupied(a, x, y) >= 5:
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