import timeit
import re

with open('input.txt') as f:
    lines = f.read().splitlines()
    g = [list(re.sub(r'[^XMAS]', '.', l)) for l in lines]
    print(g)

dirs = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
chars = ['X', 'M', 'A', 'S']


def check_dir(y, x, d):
    for next_char in chars[1:]:
        next_y = y + d[1]
        next_x = x + d[0]
        if not 0 <= next_x < len(g[0]) or not 0 <= next_y < len(g):
            return 0

        if g[next_y][next_x] != next_char:
            return 0
        y = next_y
        x = next_x

    # print("found at ", y - 3 * (d[1]), x - 3 * (d[0]), d)
    return 1


def search_at(g, y, x):
    count = 0

    for d in dirs:
        count += check_dir(y, x, d)

    return count


def f():
    count = 0

    for y in range(len(g)):
        for x in range(len(g[0])):
            if g[y][x] != "X":
                continue
            count += search_at(g, y, x)

    print(count)
    return count


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
