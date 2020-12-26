from sys import stdin
stdin = open("input.txt", "r")

def parse(line):
    lr, rr = 0, 127
    lc, rc = 0, 7
    for ch in line:
        if ch == 'F':
            rr = (lr + rr) // 2
        elif ch == 'B':
            lr = (lr + rr) // 2 + 1
        elif ch == 'L':
            rc = (lc + rc) // 2
        elif ch == 'R':
            lc = (lc + rc) // 2 + 1
    return lr, lc

def seat_id(seat):
    row, column = seat
    return row * 8 + column

seats = [seat_id(parse(line)) for line in stdin]
available = set(range(max(seats) + 1))
for seat in seats:
    available.remove(seat)

print(available)