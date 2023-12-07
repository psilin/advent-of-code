
def parse():
    cards = []
    with open('input.txt', 'r') as fh:
        for line in fh:
            card_str = line.rstrip('\n').split(':')[1]
            card_lst = card_str.split('|')
            numbers_win = set(card_lst[0].split())
            numbers = card_lst[1].split()
            cards.append((numbers_win, numbers))
    return cards


def process(cards):
    summ = 0
    for card in cards:
        cnt = 0
        for c in card[1]:
            if c in card[0]:
                cnt +=1
        
        if cnt > 0:
            summ += 2 **(cnt-1)
    return summ


def process_advanced(cards):
    count_cards = []
    for i in range(len(cards)):
        count_cards.append(1)

    for i in range(len(count_cards)):
        cnt = 0
        for c in cards[i][1]:
            if c in cards[i][0]:
                cnt +=1

        if cnt > 0:
            for j in range(cnt):
                count_cards[i + 1 + j] += count_cards[i]
    return sum(count_cards)


def main():
    cards = parse()
    print(process(cards))
    print(process_advanced(cards))


if __name__ == '__main__':
    main()