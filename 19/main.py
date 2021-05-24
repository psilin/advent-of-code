
"""
For solving this task I use 3 facts about rules and data:
 1. both rules 42 and 31 match exactly 8-letter words
 2. for task A rule 0 looks like (42, 42, 31) which means that only words of length 24 matches
 3. for task B rule 0 looks like rule 42 matches at least first half + 1 of 8-letter blocks 
    and the rest 8-letter blocks need to match rule 31

Naive match can be improved given that most of the rules just matches on letter in word and redirects
to next such rule but it is more then enough given above 3 facts. 
"""

import re
import enum


class RuleType(enum.Enum):
    LongChoice = 0
    ShortChoice = 1
    LongLine = 2
    Transition = 3
    Leaf = 4


def parse_input():
    data = []
    rules = {}
    with open('./input.txt', 'r') as fh:
        dt = False
        for line in fh:
            line = line.strip('\n')
            if line == '':
                dt = True
                continue
            if dt is False:
                m = re.match('^(\d+): (\d+) (\d+) \| (\d+) (\d+)', line)
                if m is not None:
                    rules[int(m.group(1))] = ((int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))), RuleType.LongChoice)
                    continue
                m = re.match('^(\d+): (\d+) \| (\d+)', line)
                if m is not None:
                    rules[int(m.group(1))] = ((int(m.group(2)), int(m.group(3))), RuleType.ShortChoice)
                    continue
                m = re.match('^(\d+): (\d+) (\d+)', line)
                if m is not None:
                    rules[int(m.group(1))] = ((int(m.group(2)), int(m.group(3))), RuleType.LongLine)
                    continue                
                m = re.match('^(\d+): (\d+)', line)
                if m is not None:
                    rules[int(m.group(1))] = (int(m.group(2)), RuleType.Transition)
                    continue
                m = re.match('^(\d+): \"(\w)\"', line)
                if m is not None:
                    rules[int(m.group(1))] = (str(m.group(2)), RuleType.Leaf)
                    continue
            else:
                data.append(line)
    
    rules_arr = [None, ] * len(rules)
    for r, k in rules.items():
        rules_arr[r] = k
    return rules_arr, data


def naive_match(string, rule_number, rules):
    rule_data, rule_type = rules[rule_number]
    #print(string, rule_number, rule_data, rule_type)
    if rule_type == RuleType.LongChoice:
        for i in range(1, len(string)):
            if naive_match(string[:i], rule_data[0], rules) is True and naive_match(string[i:], rule_data[1], rules) is True:
                return True        
        for i in range(1, len(string)):
            if naive_match(string[:i], rule_data[2], rules) is True and naive_match(string[i:], rule_data[3], rules) is True:
                return True
        return False

    elif rule_type == RuleType.ShortChoice:
        return naive_match(string, rule_data[0], rules) or naive_match(string, rule_data[1], rules)

    elif rule_type == RuleType.LongLine:
        for i in range(1, len(string)):
            if naive_match(string[:i], rule_data[0], rules) is True and naive_match(string[i:], rule_data[1], rules) is True:
                return True
        return False

    elif rule_type == RuleType.Transition:
        return naive_match(string, rule_data, rules)

    elif rule_type == RuleType.Leaf:
        return string == rule_data
    
    raise RuntimeError


def type_a_match(d, rules):
    if len(d) > 24:
        return False
    return all([naive_match(d[0:8], 42, rules), naive_match(d[8:16], 42, rules), naive_match(d[16:24], 31, rules)])


def type_b_match(d, rules):
    blocks = len(d)//8
    for b42 in range(blocks//2 + 1, blocks):
        tmp_res = []
        for i in range(b42):
            tmp_res.append(naive_match(d[i*8: (i+1)*8], 42, rules))
        for j in range(b42, blocks):
            tmp_res.append(naive_match(d[j*8: (j+1)*8], 31, rules))
        if all(tmp_res) is True:
            return True
    return False


if __name__ == '__main__':
    rules, data = parse_input()

    cnt_a = 0
    cnt_b = 0
    for d in data:
        res_a = type_a_match(d, rules)
        if res_a is True:
            cnt_a = cnt_a + 1

        res_b = type_b_match(d, rules)
        if res_b is True:
            cnt_b = cnt_b + 1

        print(res_a, res_b, d)

    print(cnt_a, cnt_b)
