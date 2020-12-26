from sys import stdin
stdin = open("input.txt", "r")

def parse(line):
    chunks = line.split()
    return chunks[0], int(chunks[1])
    
commands = [parse(line) for line in stdin.readlines()]

def execute():
    acc = 0
    pos = 0
    seen = [False] * len(commands)
    while pos < len(commands) and not seen[pos]:
        seen[pos] = True
        cmd, val = commands[pos]
        if cmd == 'acc':
            acc += val
            pos += 1
        elif cmd == 'jmp':
            pos += val
        else:
            pos += 1
    
    return acc, pos < len(commands)

for idx, descr in enumerate(commands):
    command, val = descr
    old_command = command
    if command == 'nop':
        commands[idx] = ['jmp', val]
    elif command == 'jmp':
        commands[idx] = ['nop', val]
    elif command == 'acc':
        continue
    acc, has_cycle = execute()
    if not has_cycle:
        print(acc)
        exit()
    commands[idx] = [old_command, val]
        