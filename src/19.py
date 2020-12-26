import numpy as np

from collections import defaultdict
from sys import stdin
from tqdm import tqdm

stdin = open("input.txt", "r")

rules = defaultdict(list)

while (line := stdin.readline()) != '\n':
    num, rule_s = line.split(':')
    if rule_s in [" \"a\"\n", " \"b\"\n"]:
        rule = rule_s[2]
    else:
        rule = [[int(v) for v in s.split()] for s in rule_s.split('|')]
    rules[int(num)] = rule

def match(s, rule_idx, l, r):
    if dp[rule_idx, l, r] != -1:
        return dp[rule_idx, l, r]
    if rules[rule_idx][0] in ['a', 'b']:
        dp[rule_idx, l, r] = (l == r and s[l] == rules[rule_idx][0])
        return dp[rule_idx, l, r]
    for rule in rules[rule_idx]:
        if len(rule) == 1:
            if match(s, rule[0], l, r):
                dp[rule[0], l, r] = 1
                return dp[rule[0], l, r]
        elif len(rule) == 2:
            rule1, rule2 = rule
            for pivot in range(l, r):
                if match(s, rule1, l, pivot) and match(s, rule2, pivot + 1, r):
                    dp[rule_idx, l, r] = 1
                    return dp[rule_idx, l, r]
        elif len(rule) == 3:
            rule1, rule2, rule3 = rule
            for pivot1 in range(l, r):
                for pivot2 in range(pivot1 + 1, r):
                    if match(s, rule1, l, pivot1) and match(s, rule2, pivot1 + 1, pivot2) and match(s, rule3, pivot2 + 1, r):
                        dp[rule_idx, l, r] = 1
                        return dp[rule_idx, l, r]
        else:
            assert False, len(rule)

    dp[rule_idx, l, r] = 0
    return dp[rule_idx, l, r]

res = 0
for line in tqdm(stdin):
    line = line.strip()
    dp = -np.ones((max(rules) + 1, len(line), len(line)), dtype=np.int32)
    res += match(line, 0, 0, len(line) - 1)

print(res)