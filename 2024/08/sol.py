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



def f():
    antinodes = set()
    for chr, coords in nodes.items():
        print(coords)
        for c1, c2 in itertools.combinations(coords, r=2):
            print(c1, c2)  # c2 always towards bottom right of c1
            dy = c1[0] - c2[0]
            dx = c1[1] - c2[1]
            print(dy, dx)
            anti1 = (c1[0] + dy, c1[1] + dx)
            anti2 = (c2[0] - dy, c2[1] - dx)
            antinodes.add(anti1)
            antinodes.add(anti2)
    filtered_antinodes = 0
    for y, x in antinodes:
        if 0<=y < Y and 0 <= x < X:
            filtered_antinodes += 1

    print(filtered_antinodes)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
