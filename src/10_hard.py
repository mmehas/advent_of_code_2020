from sys import stdin
stdin = open("input.txt", "r")
a = sorted([int(v) for v in stdin.readlines()])
a.append(a[-1] + 3)
a.insert(0, 0)

dp = [0] * len(a)
dp[0] = 1

for idx in range(len(a)):
    for idx2 in range(max(idx - 3, 0), idx):
        diff = a[idx] - a[idx2]
        if 0 < diff and diff <= 3:
            dp[idx] += dp[idx2]

print(dp[-1])
