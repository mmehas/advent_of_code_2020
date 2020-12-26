from sys import stdin

stdin = open("input.txt", "r")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def getPassport():
    data = {}
    while True:
        line = stdin.readline()
        if line == "\n" or (line == "" and data != {}):
            break
        if line == "":
            return None
        chunks = line.split()
        for chunk in chunks:
            key, value = chunk.split(':')
            data[key] = value
    return data

def checkRange(v, l, r):
    v = int(v)
    return l <= v and v <= r

def valid(data):
    for field in required_fields:
        if not field in data:
            return False
    if not checkRange(data['byr'], 1920, 2002):
        return False
    if not checkRange(data['iyr'], 2010, 2020):
        return False
    if not checkRange(data['eyr'], 2020, 2030):
        return False
    hgt_s = data['hgt']
    if len(hgt_s) < 3:
        return False
    hgt, units = hgt_s[:-2], hgt_s[-2:]
    if units == 'cm':
        if not checkRange(hgt, 150, 193):
            return False
    elif units == 'in':
        if not checkRange(hgt, 59, 76):
            return False
    else:
        return False
    hcl = data['hcl']
    if hcl[0] != '#' or len(hcl) != 7:
        return False
    for ch in hcl[1:]:
        if not ('0' <= ch and ch <= '9' or 'a' <= ch and ch <= 'f'):
            return False
    if data['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    pid = data['pid']
    if len(pid) != 9:
        return False
    for ch in pid:
        if not('0' <= ch and ch <= '9'):
            return False
    return True

res = 0
while True:
    passport = getPassport()
    if passport is None:
        break
    res += valid(passport)

print(res)
