from sys import stdin
stdin = open("input.txt", "r")
a = [(int(v), idx) for idx, v in enumerate(stdin.readline().strip().split(','))]
cur = len(a) - 1
last = a[-1][0]
spoken = dict(a[:-1])
target = 30000000
while cur != target - 1:
    if last in spoken:
        last_spoken = spoken[last]
        spoken[last] = cur
        last = cur - last_spoken
    else:
        spoken[last] = cur
        last = 0
    cur += 1

print(last)