from sys import stdin

stdin = open("input.txt", "r")

def doeval(line):
    tokens = line.split(' ')
    acc = int(tokens[0])
    idx = 0
    while idx < len(tokens):
        if tokens[idx] == '+':
            acc += int(tokens[idx + 1])
            idx += 2
        elif tokens[idx] == '*':
            acc *= int(tokens[idx + 1])
            idx += 2
        else:
            idx += 1
    return acc

def eval_expression(line):
    while (lidx := line.rfind('(')) != -1:
        ridx = line[lidx:].find(')') + lidx
        val = doeval(line[lidx + 1: ridx])
        line = line[:lidx] + str(val) + (line[ridx + 1:] if ridx + 1 < len(line) else '')

    return doeval(line)

print(sum([eval_expression(line) for line in stdin]))