import itertools
import timeit
from tqdm import tqdm
from multiprocessing import Pool

x, y = 0, 0
with open('input.txt') as f:
    lines = f.read().splitlines()
    # print(lines)
    g = [list(l) for l in lines]

    X = len(g[0])
    Y = len(g)
    for yi in range(Y):
        for xi in range(X):
            if g[yi][xi] == '^':
                x, y = xi, yi
                break


def p1(y, x):
    vis = set()
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # dy, dx
    dir_idx = 0
    curr_dir = dirs[dir_idx]
    vis.add((y, x, curr_dir))
    while 0 <= y + curr_dir[0] < Y and 0 <= x + curr_dir[1] < X:
        curr_dir = dirs[dir_idx % 4]
        next_y, next_x = y + curr_dir[0], x + curr_dir[1]
        next_ch = g[next_y][next_x]
        # print("@ ", next_y, next_x, curr_dir, next_ch)
        if next_ch == "#":
            dir_idx += 1
        else:
            y, x = next_y, next_x
            # vis.add((next_y, next_x))
            if (next_y, next_x, curr_dir) in vis:
                return True

    return len(vis)


def solve2(y_ob, x_ob):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    y_0, x_0 = y, x
    d_idx = 0
    vis = set()
    while True:
        if (y_0, x_0, d_idx) in vis:
            return True
        vis.add((y_0, x_0, d_idx))
        dy, dx = dirs[d_idx]
        y_1, x_1 = y_0 + dy, x_0 + dx
        if not (0 <= y_1 < Y and 0 <= x_1 < X):
            break
        if g[y_1][x_1] == '#' or (y_1 == y_ob and x_1 == x_ob):
            d_idx = (d_idx + 1) % 4
        else:
            y_0, x_0 = y_1, x_1
    return False


def wrapper(*subset):
    return sum([solve2(a, b) for a, b in subset])


def f():
    subsets = []
    for y in range(Y):
        subsets.append([(y, xi) for xi in range(X)])
    with Pool() as p:
        s = sum(p.starmap(wrapper, subsets))
        print(s)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
