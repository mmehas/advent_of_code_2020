from sys import stdin
stdin = open("input.txt", "r")
a = sorted([int(v) for v in stdin.readlines()])
a.append(a[-1] + 3)

cur = 0
diff = [0] * 4
for v in a:
    diff[v - cur] += 1
    cur = v

print(diff[1] * diff[3])