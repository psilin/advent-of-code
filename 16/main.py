
import enum
import re


class State(enum.IntEnum):
    Range = 1,
    OwnTicket = 2,
    OtherTickets = 3

def parse_input():
    state = State.Range

    rng = re.compile('^(\w+\ ?\w+): (\d+)-(\d+) or (\d+)-(\d+)')
    ranges = {}
    own_ticket = []
    tickets = []
    with open('./input.txt', 'r') as fh:
        for line in fh:
            if state == State.Range:
                if line == '\n':
                    state = State.OwnTicket
                    continue
                else:
                    m = rng.match(line)
                    ranges[m.group(1)] = [int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))]
            elif state == State.OwnTicket:
                if line == '\n':
                    state = State.OtherTickets
                    continue
                elif line == 'your ticket:\n':
                    continue
                else:
                    line = line.strip('\n')
                    for item in line.split(','):
                        own_ticket.append(int(item))
            elif state == State.OtherTickets:
                if line == 'nearby tickets:\n':
                    continue
                line = line.strip('\n')
                t = []
                for item in line.split(','):
                    t.append(int(item))
                tickets.append(t)
    return ranges, own_ticket, tickets


def find_invalid(ranges, tickets):
    invalid_fields = []
    filtered_tickets = []
    for t in tickets:
        ticket_ok = True
        for item in t:
            found = False
            for r in ranges.values():
                if r[0] <= item <= r[1] or r[2] <= item <= r[3]:
                    found = True
            if found is False:
                ticket_ok = False
                invalid_fields.append(item)
        if ticket_ok is True:
            filtered_tickets.append(t)
    return sum(invalid_fields), filtered_tickets


def process_filtered(ranges, tickets):
    dist = {}
    for r in ranges:
        for i in range(len(tickets[0])):
            idx_ok = True
            for t in tickets:
                if ranges[r][0] > t[i] or t[i] > ranges[r][1] and\
                   ranges[r][2] > t[i] or t[i] > ranges[r][3]:
                    idx_ok = False
                    break
            if idx_ok is True:
                if dist.get(r, None) is None:
                    dist[r] = [i, ]
                else:
                    dist[r].append(i)
    return dist


def process_dist(dist):
    proc_dist = {}
    while len(dist) > 0:
        for d in dist:
            if len(dist[d]) == 1:
                val = dist.pop(d)[0]
                proc_dist[d] = val
                for dd in dist:
                    dist[dd].remove(val)
                break
    return proc_dist


def mult_up(proc_dist, own_ticket):
    mult = 1
    for pd in proc_dist:
        if 'departure' in pd:
            mult *= own_ticket[proc_dist[pd]]
    return mult


if __name__ == '__main__':
    ranges, own_ticket, tickets = parse_input()
    summ, filtered_tickets = find_invalid(ranges, tickets)
    print(summ)
    dist = process_filtered(ranges, filtered_tickets)
    proc_dist = process_dist(dist)
    print(mult_up(proc_dist, own_ticket))
