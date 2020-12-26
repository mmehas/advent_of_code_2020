from sys import stdin

stdin = open("input.txt", "r")

window = 25

a = [int(v) for v in stdin.readlines()]

def valid(list, v):
    for idx1 in range(len(list)):
        for idx2 in range(idx1 + 1, len(list)):
            if list[idx1] + list[idx2] == v:
                return True
    return False

for idx in range(window, len(a)):
    if not valid(a[idx - window: idx], a[idx]):
        print(a[idx])
        exit()