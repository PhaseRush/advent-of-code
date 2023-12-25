import sys
import timeit
from collections import defaultdict, deque

# sys.setrecursionlimit(1000000)
n = (-1, 0)
e = (0, 1)
s = (1, 0)
w = (0, -1)

opposite = {
    n: s,
    s: n,
    e: w,
    w: e
}

dirs = [n, e, s, w]

with open('input.txt') as f:
    lines = f.read().splitlines()
    Y = len(lines)
    X = len(lines[0])

    graph = defaultdict(set)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '#':
                for dy, dx in dirs:
                    new_y = y + dy
                    new_x = x + dx
                    if 0 <= new_y < Y and 0 <= new_x < X and lines[new_y][new_x] != '#':
                        graph[(y, x)].add((new_y, new_x, 1))
                        graph[(new_y, new_x)].add((y, x, 1))

    # found this on reddit
    while True:
        for n, e in graph.items():
            if len(e) == 2:
                a, b = e
                graph[a[:2]].remove(n + (a[2],))
                graph[b[:2]].remove(n + (b[2],))
                graph[a[:2]].add((b[0], b[1], a[2] + b[2]))
                graph[b[:2]].add((a[0], a[1], a[2] + b[2]))
                del graph[n]
                break
        else:
            break

best = 0
print(len(graph))


def dfs(curr, path, curr_dist):
    global best
    if curr == (Y - 1, X - 2):
        best = max(best, curr_dist)
    else:
        for y, x, dist in graph[curr]:
            next = (y, x)
            if next not in path:
                path.add(next)
                dfs(next, path, curr_dist + dist)
                path.remove(next)


def f():
    dfs((0, 1), set(), 0)
    print(best)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
