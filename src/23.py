s = '167248359'
l = [int(ch) for ch in s]
    
cur_v = l[0]
for _ in range(100):
    cur_idx = l.index(cur_v)
    hold = []
    next_idx = (cur_idx + 1) % len(l)
    for _ in range(3):
        if next_idx == len(l):
            next_idx = 0
        hold.append(l[next_idx])
        del l[next_idx]
    dest_v = cur_v - 1
    while True:
        if dest_v == 0:
            dest_v = 9
        if dest_v in hold:
            dest_v -= 1
        else:
            dest_idx = (l.index(dest_v) + 1) % len(l)
            l[dest_idx:dest_idx] = hold
            cur_idx = l.index(cur_v)
            cur_v = l[(cur_idx + 1) % len(l)]
            break
l = l + l
l = ''.join(map(str, l[l.index(1) + 1 : l.index(1) + len(l) // 2]))
print(l)