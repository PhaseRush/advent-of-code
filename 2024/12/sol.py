import timeit
from collections import deque

with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)
    g = [list(l) for l in lines]
    print(g)
    Y = len(g)
    X = len(g[0])


def in_grid(y, x):
    return y in range(Y) and x in range(X)


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dirs_v = [(-1, 0), (1, 0)]
dirs_h = [(0, 1), (0, -1)]


def f():
    s = 0
    vis = set()
    for y in range(Y):
        for x in range(X):
            if (y, x) in vis:
                continue
            Q = deque([(y, x)])
            area = 0
            perim = 0

            while Q:
                curr_y, curr_x = Q.popleft()
                if (curr_y, curr_x) in vis:
                    continue
                vis.add((curr_y, curr_x))
                area += 1
                for dy, dx in dirs:
                    next_y, next_x = curr_y + dy, curr_x + dx
                    if in_grid(next_y, next_x) and g[curr_y][curr_x] == g[next_y][next_x]:
                        Q.append((next_y, next_x))
                    else:
                        perim += 1
            s += perim * area
    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
