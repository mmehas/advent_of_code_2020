from sys import stdin
stdin = open("input.txt", "r")
t_start = int(stdin.readline())
buses = [int(t) for t in stdin.readline().split(',') if t != 'x']
id, delay = min([((((t_start // id + 1) * id - t_start) % id), id) for id in buses])
print(id, delay, id * delay)