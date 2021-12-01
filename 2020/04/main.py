
import copy
import string


def parse_input():
    data = []
    passport = {}
    with open('./input.txt', 'r') as fh:
        for line in fh:
            line = line.strip('\n')
            if len(line) == 0:
                data.append(copy.deepcopy(passport))
                passport = {}
            else:
                lst = line.split(' ')
                for pair in lst:
                    res = pair.split(':')
                    passport[res[0]] = res[1]
        if passport != {}:
            data.append(passport)
    return data


def count_valid(data):
    cnt = 0
    for passp in data:
        valid = True
        for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
            if passp.get(field, None) is None:
                valid = False
        if valid is True:
            cnt += 1
    return cnt


def adv_count_valid(data):
    cnt = 0
    for passp in data:
        valid = True
        for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
            if passp.get(field, None) is None:
                valid = False

        if valid is False:
            continue

        p = passp['byr']
        if not (len(p) == 4 and p.isdigit() == True and 1920 <= int(p) <= 2002):
            continue

        p = passp['iyr']
        if not (len(p) == 4 and p.isdigit() == True and 2010 <= int(p) <= 2020):
            continue

        p = passp['eyr']
        if not (len(p) == 4 and p.isdigit() == True and 2020 <= int(p) <= 2030):
            continue

        p = passp['hgt']
        if not ((len(p) == 5 and p[3:] == 'cm' and p[:3].isdigit() and 150 <= int(p[:3]) <= 193) or (len(p) == 4 and p[2:] == 'in' and p[:2].isdigit() and 59 <= int(p[:2]) <= 76)):
            continue

        p = passp['hcl']
        if not (len(p) == 7 and p[0] == '#' and all(c in string.hexdigits for c in p[1:])):
            continue 

        p = passp['ecl']
        if not (p in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')):
            continue

        p = passp['pid']
        if not (len(p) == 9 and p.isdigit() == True):
            continue

        cnt += 1
    return cnt



if __name__ == '__main__':
    data = parse_input()
    print(count_valid(data))
    print(adv_count_valid(data))
