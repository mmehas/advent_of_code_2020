from sys import stdin
stdin = open("input.txt", "r")

def get_deck():
    stdin.readline()
    d = []
    while (line := stdin.readline()) != '\n':
        d.append(int(line))
    return d

d1, d2 = get_deck(), get_deck()

def game(d1, d2):
    seen = set()
    while True:
        state = tuple([tuple(d1), tuple(d2)])
        if state in seen:
            return 0, None
        seen.add(state)
        top1, top2 = d1.pop(0), d2.pop(0)
        if top1 > len(d1) or top2 > len(d2):
            winner = 0 if top1 > top2 else 1
        else:
            winner, _ = game(d1[:top1], d2[:top2])
        if winner == 0:
            d1.extend([top1, top2])
        else:
            d2.extend([top2, top1])
        if len(d1) == 0:
            return 1, d2
        if len(d2) == 0:
            return 0, d1

res, win_d = game(d1, d2)
print(res, win_d)
print(sum([(idx + 1) * v for idx, v in enumerate(win_d[::-1])]))
