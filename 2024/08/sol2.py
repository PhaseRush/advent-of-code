import timeit
from collections import defaultdict
import itertools

with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)
    nodes = defaultdict(list)
    Y = len(lines)
    X = len(lines[0])
    for y in range(Y):
        for x in range(X):
            chr = lines[y][x]
            if chr != ".":
                nodes[chr].append((y, x))

    print(nodes)


# c2 always towards bottom right of c1
def add_all(c1, c2) -> set:
    dy = c1[0] - c2[0]
    dx = c1[1] - c2[1]
    to_ret = {c1, c2}
    curr_iter = 1
    while True:
        anti1_y = c1[0] + dy * curr_iter
        anti1_x = c1[1] + dx * curr_iter
        curr_iter += 1
        if not (anti1_x in range(X) and anti1_y in range(Y)):
            break
        to_ret.add((anti1_y, anti1_x))
    curr_iter = 1
    while True:
        anti2_y = c2[0] - dy * curr_iter
        anti2_x = c2[1] - dx * curr_iter
        curr_iter += 1
        if not (0 <= anti2_x < X and 0 <= anti2_y < Y):
            break
        to_ret.add((anti2_y, anti2_x))
    return to_ret


def f():
    antinodes = set()
    for _, coords in nodes.items():
        for c1, c2 in itertools.combinations(coords, r=2):
            antinodes |= add_all(c1, c2)
    print(len(antinodes))
    return len(antinodes)


if __name__ == '__main__':
    iters = 10
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.4f} s")
