from sys import stdin

stdin = open("input.txt", "r")

a = sorted([int(v) for v in stdin.readlines() if v != ""])

target = 2020

l = 0
r = len(a) - 1

while l < r:
    if a[l] + a[r] > target:
        r -= 1
    elif a[l] + a[r] == target:
        if l < r:
            print(a[l] * a[r])
        break
    else:
        l += 1