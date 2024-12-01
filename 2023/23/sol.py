import sys
import timeit
from collections import defaultdict

sys.setrecursionlimit(1000000)
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
            if char == '.':
                for dy, dx in dirs:
                    new_y = y + dy
                    new_x = x + dx
                    if 0 <= new_y < Y and 0 <= new_x < X and lines[new_y][new_x] == '.':
                        graph[(y, x)].add((new_y, new_x))
                        graph[(new_y, new_x)].add((y, x))
            elif char == 'v':
                graph[(y, x)].add((y + 1, x))
                graph[(y - 1, x)].add((y, x))
            elif char == '>':
                graph[(y, x)].add((y, x + 1))
                graph[(y, x - 1)].add((y, x))

best = 0


def dfs(curr, path, visited):
    global best
    if curr == (Y - 1, X - 2):
        best = max(best, len(path))
    else:
        for edge in graph.get(curr):
            if edge not in visited:
                path.append(edge)
                visited.add(edge)
                dfs(edge, path, visited)
                visited.remove(edge)
                path.pop()


def f():
    dfs((0, 1), [], set())
    print(best)


# print(lines)

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
