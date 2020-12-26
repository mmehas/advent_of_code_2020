from sys import stdin
stdin = open("input.txt", "r")

rules = []

def conforms(v, rule):
    for l, r in rule:
        if l <= v and v <= r:
            return True
    return False

while (line := stdin.readline()) != '\n':
    rules.append([])
    name, restrictions = line.split(':')
    for rule in restrictions.split(' or '):
        l, r = rule.split('-')
        rules[-1].append((int(l), int(r)))
stdin.readline()
my_ticket = [int(v) for v in stdin.readline().strip().split(',')]
stdin.readline()
stdin.readline()

nearby_tickets = []
for line in stdin:
    nearby_tickets.append([int(v) for v in line.strip().split(',')])

res = 0
stdout = open("tickets.txt", "w")
for ticket in nearby_tickets:
    ticket_validated = True
    for v in ticket:
        validated = False
        for rule in rules:
            if conforms(v, rule):
                validated = True
                break
        res += (1 - validated) * v
        ticket_validated &= validated
    if ticket_validated:
        ticket_str = ','.join([str(v) for v in ticket])
        stdout.writelines(ticket_str)
        stdout.write('\n')

stdout.close()
print(res)
