from sys import stdin

stdin = open("input.txt", "r")
target = 556543474

a = [int(v) for v in stdin.readlines()]
r = 0
s = a[0]
for idx in range(len(a)):
    while r < len(a) - 1 and s + a[r + 1] <= target:
        r += 1
        s += a[r]
    if s == target:
        print(min(a[idx: r + 1]) + max(a[idx: r + 1]))
        exit()
    s -= a[idx]
