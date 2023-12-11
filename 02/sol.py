import timeit
from collections import defaultdict


def f():
    valid_games = []

    def compute_power(outcome: str):
        inv = defaultdict(int)
        for game in outcome.split(";"):
            draws = game.split(",")
            for draw in draws:
                num, color = draw.strip().split(" ")
                inv[color] = max(inv[color], int(num))

        # print(inv['red'] * inv['blue'] * inv['green'])
        return inv['red'] * inv['blue'] * inv['green']

    with open('input.txt') as f:
        for line in f:
            _, outcome = line.rstrip().split(":")
            valid_games.append(compute_power(outcome))

    return sum(valid_games)


# print(timeit.timeit(f, number=1000))
print(f())
