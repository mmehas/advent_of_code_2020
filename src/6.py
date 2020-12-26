from sys import stdin
stdin = open("input.txt", "r")

res = 0
seen = set()
for line in stdin:
    if line == '' or line == '\n':
        res += len(seen)
        seen = set()
    else:
        for ch in line:
            if ch != '\n':
                seen.add(ch)
res += len(seen)
print(res)
    