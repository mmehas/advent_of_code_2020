from sys import stdin, stdout
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching

stdin = open("input.txt", "r")

rules = []
rule_name = []

def conforms(v, rule):
    for l, r in rule:
        if l <= v and v <= r:
            return True
    return False
    
while (line := stdin.readline()) != '\n':
    rules.append([])
    name, restrictions = line.split(':')
    rule_name.append(name)
    for rule in restrictions.split(' or '):
        l, r = rule.split('-')
        rules[-1].append((int(l), int(r)))

stdin.readline()
my_ticket = [int(v) for v in stdin.readline().strip().split(',')]
stdin.readline()
stdin.readline()

nearby_tickets = [my_ticket]
for line in stdin:
    nearby_tickets.append([int(v) for v in line.strip().split(',')])

conformity = [[True] * len(my_ticket) for _ in range(len(rules))]
for rule_idx, rule in enumerate(rules):
    for field_idx, value in enumerate(my_ticket):
        for ticket in nearby_tickets:
            if not conforms(ticket[field_idx], rule):
                conformity[rule_idx][field_idx] = False
                break

G = csr_matrix(conformity)
matching = maximum_bipartite_matching(G, perm_type='column')

res = 1
for idx, name in enumerate(rule_name):
    if 'departure' in name:
        res *= my_ticket[matching[idx]]
print(res)