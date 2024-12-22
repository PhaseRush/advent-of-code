import itertools
import timeit

with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)
    grid = [list(r) for r in lines]

    for ir, r in enumerate(grid):
        for ic, c in enumerate(r):
            if c == "S":
                start = (ir, ic)

    Y = len(grid)
    X = len(grid[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs():
    costs = {start: 0}
    q = [start]

    for (y_0, x_0) in q:
        for d in dirs:
            y_1, x_1 = y_0 + d[0], x_0 + d[1]
            if y_1 in range(Y) and x_1 in range(X) and grid[y_1][x_1] != "#":
                if (y_1, x_1) not in costs:
                    costs[(y_1, x_1)] = costs[(y_0, x_0)] + 1
                    q.append((y_1, x_1))

    return costs


def f():
    costs = bfs()

    s = 0
    for ((y_a, x_a), c_a), ((y_b, x_b), c_b) in itertools.combinations(costs.items(), 2):
        # print(y_a, x_a, c_a)
        manhattan = abs(y_a - y_b) + abs((x_a - x_b))
        if manhattan < 21 and c_b - c_a - manhattan >= 100: s += 1

    print(s)
    return s

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
