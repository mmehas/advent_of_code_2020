from sys import stdin
import re

stdin = open("input.txt", "r")

def parse(line):
    chunks = re.split(':| |-|\n', line)
    l = int(chunks[0])
    r = int(chunks[1])
    ch = chunks[2]
    s = chunks[4]
    cnt = 0
    for c in s:
        if c == ch:
            cnt +=1
    return l <= cnt  and cnt <= r

print(sum([parse(line) for line in stdin.readlines()]))