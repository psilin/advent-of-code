
def parse():
    games = []
    with open("./input.txt", "r") as fh:
        for line in fh:
            gms = line.rstrip("\n").split(":")[1].split(";")
            game = []
            for g in gms:
                g_dict = {}
                gs = g.split(",")
                for gg in gs:
                    gg = gg.split()
                    g_dict[gg[1]] = int(gg[0])
                game.append(g_dict)
            games.append(game) 
    return games


def process(games):
    summ = 0
    for i in range(len(games)):
        for rnd in games[i]:
            if rnd.get("red", 0) > 12 or rnd.get("green", 0) > 13 or rnd.get("blue", 0) > 14:
                break
        else:
            summ += (i + 1)
    return summ 


def process_advanced(games):
    summ = 0
    for game in games:
        r, g, b = 0, 0, 0
        for round in game:
            r = max(r, round.get("red", 0))
            g = max(g, round.get("green", 0))
            b = max(b, round.get("blue", 0))
        summ += r*g*b
    return summ


def main():
    games = parse()
    print(process(games))
    print(process_advanced(games))


if __name__ == "__main__":
    main()
