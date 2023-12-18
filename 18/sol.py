import timeit
import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()
    lines = [l.split() for l in lines]
    # lines = [(x[0], int(x[1]), int(x[2][2:-1], 16)) for x in lines]
    lines = [(x[0], int(x[1]), x[2][2:-1]) for x in lines]

dirs = {
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0),
    '0': (0, 1),
    '1': (1, 0),
    '2': (0, -1),
    '3': (-1, 0)
}


def PolyArea(x, y):
    x = np.asarray(x, dtype='int64')
    y = np.asarray(y, dtype='int64')
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


def move(pos, dir, amount):
    dir = dirs[dir]
    return pos[0] + dir[0] * amount, pos[1] + dir[1] * amount


def f():
    pos = (0, 0)
    vertices = {(0, 0)}
    xs = []
    ys = []

    for dir, _, colour in lines:
        # pt 2:
        dir = dirs[colour[-1]]
        amount = int(colour[:-1], 16)

        # dir = dirs[dir]
        for i in range(amount + 1):
            vertices.add((pos[0] + i * dir[0], pos[1] + i * dir[1]))
        pos = (pos[0] + amount * dir[0], pos[1] + amount * dir[1])
        xs.append(pos[0])
        ys.append(pos[1])

    area = PolyArea(xs, ys)
    b = len(vertices)
    print((area + 1 - b // 2) + b)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
