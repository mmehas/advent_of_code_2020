from sys import stdin
from math import pi, cos, sin, atan2

stdin = open("input.txt", "r")
commands = [(l[0], int(l[1:].strip())) for l in stdin]

x, y, dx, dy = 0, 0, 10, 1

for cmd, val in commands:
    if cmd == 'N':
        dy += val
    elif cmd == 'S':
        dy -= val
    elif cmd == 'W':
        dx -= val
    elif cmd == 'E':
        dx += val
    elif cmd == 'L':
        angle = atan2(dy, dx)
        val = val / 360.0 * 2 * pi
        l = (dx ** 2 + dy ** 2) ** 0.5
        angle = angle + val
        dx, dy = l * cos(angle), l * sin(angle)
    elif cmd == 'R':
        angle = atan2(dy, dx)
        val = val / 360.0 * 2 * pi
        l = (dx ** 2 + dy ** 2) ** 0.5
        angle = angle - val
        dx, dy = l * cos(angle), l * sin(angle)
    else:
        x, y = x + dx * val, y + dy * val

print(abs(x) + abs(y))