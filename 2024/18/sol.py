import timeit
from collections import deque
from bisect import bisect

with open('input.txt') as f:
    lines = f.read().splitlines()
    # print(lines)
    parsed = [tuple(map(int, line.split(","))) for line in lines]
    print(parsed)

    Y = 71
    X = 71

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(idx):
    seen = {*parsed[:idx]}
    todo = deque()
    todo.append((0, (0, 0)))
    # todo = [(0, (0,0))]
    while todo:
        curr_dist, (x, y) = todo.popleft()
        # for curr_dist, (x, y) in todo:
        if (x, y) == (70, 70):
            return curr_dist

        for d in dirs:
            x_1, y_1 = x + d[1], y + d[0]  # wack order
            if (x_1, y_1) not in seen and x_1 in range(X) and y_1 in range(Y):
                todo.append((curr_dist + 1, (x_1, y_1)))
                seen.add((x_1, y_1))

    return 1_000_000


def f():
    print(bfs(1024))
    print(parsed[bisect(range(len(parsed)), 1e9 - 1, key=bfs) - 1])


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
