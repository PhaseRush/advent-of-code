import math
import timeit
import re
import numpy as np
from tqdm import tqdm

with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)

    X = 101
    Y = 103

    mat = np.zeros((Y, X))
    matx = np.zeros(X)
    maty = np.zeros(Y)

    bots = []
    for l in lines:
        nums = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", l)
        coords = list(map(int, nums[0]))
        bots.append(coords)
        mat[coords[1] % Y, coords[0] % X] = 1
        maty[coords[1] % Y] = 1
        matx[coords[0] % X] = 1

    print(bots)

    # X = 11
    # Y = 7


def sim():
    mat.fill(0)
    matx.fill(0)
    maty.fill(0)
    for b in bots:
        b[0] = (b[0] + b[2]) % X
        b[1] = (b[1] + b[3]) % Y
        mat[b[1], b[0]] = 1
        matx[b[0]] = 1
        maty[b[1]] = 1


def count():
    top_left = 0
    top_right = 0
    bot_left = 0
    bot_right = 0
    for b in bots:
        x = b[0] % X
        y = b[1] % Y
        if x == (X - 1) // 2:
            continue
        if y == (Y - 1) // 2:
            continue
        left = x < X // 2
        top = y < Y // 2
        if top and left:
            top_left += 1
        elif top and not left:
            top_right += 1
        elif not top and left:
            bot_left += 1
        elif not top and not left:
            bot_right += 1

    # print(top_left, top_right, bot_left, bot_right)
    return top_left, top_right, bot_left, bot_right


def components():
    pass

def f():
    stds = []
    safeties = []
    for i in tqdm(range(X * Y)):
        sim()
        if i == 8052:
            printx()
        std = mat.var()
        stdx = matx.var()
        stdy = maty.var()
        # print(i, std)
        stds.append((i, std, stdx, stdy))
        # input()
        safety = math.prod(count())
        safeties.append((i, safety))

    print("std: ", min(stds, key=lambda x: x[1]))
    print("stdx: ", min(stds, key=lambda x: x[2]))
    print("stdy: ", min(stds, key=lambda x: x[3]))
    print("safety: ", min(safeties, key=lambda x: x[1]))


def printx():
    canvas = [['.'] * X for x in range(Y)]
    for bx, by, _, _ in bots:
        canvas[by % Y][bx % X] = '@'
    for row in canvas:
        print(''.join(row))


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
