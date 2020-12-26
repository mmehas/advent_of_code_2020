from sys import stdin

from collections import defaultdict

stdin = open("input.txt", "r")

def chunker(l, k):
    return [l[idx : idx + k] for idx in range(0, len(l), k)]

def parse(line):
    chunks = line.split()
    s = ' '.join(chunks[:2])
    children = []
    if chunks[4] != 'no':
        for _, c1, c2, _ in chunker(chunks[4:], 4):
            children.append(' '.join([c1, c2]))
    return s, children
        
def dfs(g, v):
    res = {v}
    for w in g[v]:
        res = res.union(dfs(g, w))
    return res

g = defaultdict(set)
for line in stdin:
    s, children = parse(line)
    for child in children:
        g[child].add(s)

print(len(dfs(g, 'shiny gold')) - 1)
