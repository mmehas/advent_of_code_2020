from sys import stdin
stdin = open("input.txt", "r")

def parse(line):
    chunks = line.split()
    return chunks[0], int(chunks[1])
    
commands = [parse(line) for line in stdin.readlines()]

acc = 0
pos = 0
seen = [False] * len(commands)

while not seen[pos]:
    seen[pos] = True
    cmd, val = commands[pos]
    if cmd == 'acc':
        acc += val
        pos += 1
    elif cmd == 'jmp':
        pos += val
    else:
        pos += 1

print(acc)
