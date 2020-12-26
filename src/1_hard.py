from sys import stdin

stdin = open("input.txt", "r")

a = sorted([int(v) for v in stdin.readlines() if v != ""])

target = 2020

def solve(a, l, r, target):
    while l < r:
        if a[l] + a[r] > target:
            r -= 1
        elif a[l] + a[r] == target:
            if l < r:
                return a[l], a[r]
            return None
        else:
            l += 1

l = len(a) - 1

for idx in range(0, len(a)):
    res = solve(a, idx + 1, l, target - a[idx])
    if res is not None:
        print(a[idx] * res[0] * res[1])
        break