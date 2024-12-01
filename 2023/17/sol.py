import timeit
from collections import defaultdict

from heapq import heappop, heappush

with open('input.txt') as f:
    lines = [[int(n) for n in y] for y in f.read().splitlines()]

Y = len(lines)
X = len(lines[0])

n = (-1, 0)
e = (0, 1)
s = (1, 0)
w = (0, -1)
dirs = [n, e, s, w]

dir_index = {
    n: 0,
    e: 1,
    s: 2,
    w: 3
}

dir_bin = {
    n: 1,
    e: 2,
    s: 4,
    w: 8
}

opposite = {
    n: s,
    s: n,
    e: w,
    w: e
}


def simulate(min_dist, max_dist):
    # cost, x, y, from_dir
    q = [(0, 0, 0, w)]
    visited = [0] * (Y * X)
    costs = defaultdict(lambda: 10e3)
    while q:
        cost, x, y, from_dir = heappop(q)
        if x == X - 1 and y == Y - 1:
            return cost
        if visited[y * X + x] >> dir_index[from_dir] & 1:
            continue
        visited[y * X + x] |= dir_bin[from_dir]

        for new_dir in dirs:
            if new_dir == from_dir:
                continue

            extra_cost = 0
            for dist in range(1, max_dist + 1):
                new_x = x + new_dir[0] * dist
                new_y = y + new_dir[1] * dist
                if 0 <= new_x < X and 0 <= new_y < Y:
                    extra_cost += lines[new_x][new_y]
                    if dist < min_dist:
                        continue
                    total_cost = cost + extra_cost
                    if costs[(new_x, new_y, new_dir)] > total_cost:
                        costs[(new_x, new_y, new_dir)] = total_cost
                        heappush(q, (total_cost, new_x, new_y, new_dir))


def f():
    # print(simulate(1, 3))
    print(simulate(4, 10))


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
