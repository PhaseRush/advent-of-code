import functools
import timeit

with open('input.txt') as f:
    lines = [list(x) for x in f.read().splitlines()]


def hash_mat(mat):
    hid = tuple(tuple(x) for x in mat)
    return hid


def rotate_matrix(m):
    rot = zip(*m[::-1])
    return [list(x) for x in rot]


# @functools.cache
def shift(mat):
    for x in range(len(mat[0])):
        for y_start in range(len(mat)):  # be naive and just shift every possibility
            for y_curr in range(len(mat)):
                if y_curr > 0:
                    if mat[y_curr][x] == 'O' and mat[y_curr - 1][x] == '.':
                        mat[y_curr - 1][x] = 'O'
                        mat[y_curr][x] = '.'
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
    # cycles = 1

    cache = {}

    curr_idx = 0
    mat = lines
    while curr_idx < cycles:
        curr_idx += 1
        for j in range(4):
            mat = shift(mat)
            mat = rotate_matrix(mat)
        hash_id = hash_mat(mat)
        if hash_id in cache:
            cycle_length = curr_idx - cache[hash_id]
            num_cycles = (cycles - curr_idx) // cycle_length
            # print(curr_idx, cycle_length)
            curr_idx += num_cycles * cycle_length
        cache[hash_id] = curr_idx
    print(count_load(mat))


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
