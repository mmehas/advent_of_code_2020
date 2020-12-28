from sys import stdin
stdin = open("input.txt", "r")

def get_deck():
    stdin.readline()
    d = []
    while (line := stdin.readline()) != '\n':
        d.append(int(line))
    return d

d1, d2 = get_deck(), get_deck()

while len(d1) != 0 and len(d2) != 0:
    top1, top2 = d1.pop(0), d2.pop(0)
    if top1 > top2:
        d1.extend([top1, top2])
    else:
        d2.extend([top2, top1])

win_d = d1 if len(d1) !=0 else d2
print(sum([(idx + 1) * v for idx, v in enumerate(win_d[::-1])]))
