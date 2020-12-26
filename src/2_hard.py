from sys import stdin
import re

stdin = open("input.txt", "r")

def parse(line):
    chunks = re.split(':| |-|\n', line)
    l = int(chunks[0]) - 1
    r = int(chunks[1]) - 1
    ch = chunks[2]
    s = chunks[4]
    return (s[l] == ch) != (s[r] == ch)

print(sum([parse(line) for line in stdin.readlines()]))