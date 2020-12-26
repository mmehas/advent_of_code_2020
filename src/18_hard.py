import numpy as np
from sys import stdin

stdin = open("input.txt", "r")

def doeval(line):
    tokens = line.split(' ')
    
    while '+' in tokens:
        idx = tokens.index('+')
        tokens[idx - 1] = int(tokens[idx - 1]) + int(tokens[idx + 1])
        del tokens[idx]
        del tokens[idx]
    return np.prod([int(v) for v in tokens if v != '*'])

def eval_expression(line):
    while (lidx := line.rfind('(')) != -1:
        ridx = line[lidx:].find(')') + lidx
        val = doeval(line[lidx + 1: ridx])
        line = line[:lidx] + str(val) + (line[ridx + 1:] if ridx + 1 < len(line) else '')

    return doeval(line)

print(sum([eval_expression(line) for line in stdin]))