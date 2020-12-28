from sys import stdin
stdin = open("input.txt", "r")

mod = 20201227
key1 = int(stdin.readline())
key2 = int(stdin.readline())

def power(base, exp, mod):
    res = 1
    for _ in range(exp):
        res = (res * base) % mod
    return res

def find_exponent(base, res, mod):
    cur = base
    cnt = 1
    while True:
        if cur == res:
            return cnt
        cur = (cur * base) % mod
        cnt += 1

b1 = find_exponent(7, key1, mod)
encryption_key = power(key2, b1, mod)

print(encryption_key)