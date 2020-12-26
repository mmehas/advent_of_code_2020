from sys import stdin
stdin = open("input.txt", "r")

res = 0
in_group = 0
seen = {chr(key): 0 for key in range(ord('a'), ord('z') + 1)}
for line in stdin:
    if line == '' or line == '\n':
        res += sum([v == in_group for v in seen.values()])
        seen = {chr(key): 0 for key in range(ord('a'), ord('z') + 1)}
        in_group = 0
    else:
        in_group += 1
        for ch in line:
            if ch != '\n':
                seen[ch] += 1
res += sum([v == in_group for v in seen.values()])
print(res)
    