from sys import stdin

stdin = open("input.txt", "r")
a = stdin.readlines()

x, y = 0, 0
n = len(a)
w = len(a[0]) - 1
res = 0
while x < n:
    res += a[x][y] == '#'
    x += 1
    y = (y + 3) % w

print(res)