from sys import stdin
import numpy as np

stdin = open("input.txt", "r")
t_start = int(stdin.readline())
buses = [(int(t), -id) for id, t in enumerate(stdin.readline().split(',')) if t != 'x']


def crt(eq):
    n, a = zip(*eq)
    print(n, a)
    sum = 0
    prod = np.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

sol = crt(buses)
print(sol)