import functools
import timeit

import util.utils

with open('input.txt') as f:
    lines = [list(x) for x in f.read().splitlines()]


def hash_mat(mat):
    hid = tuple(tuple(x) for x in mat)
    return hid


def locate_cubes(col):
    indices = []
    i = 0
    while True:
        try:
            i = col.index('#', i)
            indices.append(i)
            i += 1
        except ValueError:
            break
    return indices


def shift_col(col):
    cube_idxs = [-1] + [i for i, x in enumerate(col) if x == "#"] + [len(col)]
    # cube_idxs = [-1] + locate_cubes(col) + [len(col)]

    for idx in range(len(cube_idxs) - 1):
        curr_start = cube_idxs[idx] + 1
        curr_end = cube_idxs[idx + 1]

        num_round = 0
        for i in range(curr_start, curr_end):
            num_round += col[i] == 'O'

        for i in range(curr_start, curr_start + num_round):
            col[i] = 'O'

        for i in range(curr_start + num_round, curr_end):
            col[i] = '.'

    return col


def shift(mat):
    for y in range(len(mat)):
        mat[y] = shift_col(mat[y])
    return mat


def show(mat):
    for i in range(len(mat)):
        print(mat[i])


def count_load(shifted):
    load = 0
    n = len(shifted)
    for i in range(n):
        for j in range(len(shifted[0])):
            if shifted[i][j] == 'O':
                load += n - i
    return load


def f():
    cycles = 1000000000
    cache = {}

    curr_idx = 0
    mat = util.utils.rotate_ccw(lines)
    while curr_idx < cycles:
        curr_idx += 1
        for j in range(4):
            mat = shift(mat)
            mat = util.utils.rotate_cw(mat)
        hash_id = hash_mat(mat)
        if hash_id in cache:
            cycle_length = curr_idx - cache[hash_id]
            num_cycles = (cycles - curr_idx) // cycle_length
            curr_idx += num_cycles * cycle_length
        cache[hash_id] = curr_idx
    mat = util.utils.rotate_cw(mat)
    print(count_load(mat))


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
