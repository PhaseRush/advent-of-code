import functools
import time
from itertools import chain, product
import multiprocessing
import timeit
from collections import deque
from multiprocessing import Pool, cpu_count

with open('input.txt') as f:
    lines = f.read().splitlines()

Y = len(lines)
X = len(lines[0])

n = (-1, 0)
e = (0, 1)
s = (1, 0)
w = (0, -1)


def move(pos, dir):
    return pos[0] + dir[0], pos[1] + dir[1]


dir_index = {
    n: 0,
    e: 1,
    s: 2,
    w: 3
}

choice = {
    '.': [[n], [e], [s], [w]],
    '/': [[e], [n], [w], [s]],
    '\\': [[w], [s], [e], [n]],
    '|': [[n], [n, s], [s], [n, s]],
    '-': [[e, w], [e], [e, w], [w]]
}

visited_edge = set()

opposite = {
    n: s,
    s: n,
    e: w,
    w: e
}


def get(pos, dir):
    if pos[0] < 0 or pos[0] >= Y or pos[1] < 0 or pos[1] >= X:
        # trying to exit
        visited_edge.add(move(pos, opposite[dir]))
        return None
    return lines[pos[0]][pos[1]]


dir_bin = {
    n: 1,
    e: 2,
    s: 4,
    w: 8
}


def simulate(init_pos, init_dir):
    if init_pos in visited_edge:
        return -1

    visited = [0] * Y * X
    count = 0

    q = deque([(init_pos, init_dir)])
    while q:
        pos, dir = q.popleft()
        curr_char = get(pos, dir)
        if not curr_char:
            continue

        if not visited[pos[0] * X + pos[1]]:
            count += 1

        if not (visited[pos[0] * X + pos[1]] >> dir_index[dir] & 1):
            visited[pos[0] * X + pos[1]] |= dir_bin[dir]
            new_dirs = choice[curr_char][dir_index[dir]]
            for new_dir in new_dirs:
                q.append((move(pos, new_dir), new_dir))

    return count


def f():
    best = -1
    for y in range(len(lines)):
        # for y in [0, Y]:
        #     for x in range(len(lines[0])):
        for x in [0, X]:
            init_pos = (y, x)
            init_dirs = []
            if y == 0:
                init_dirs.append(s)
            elif y == len(lines) - 1:
                init_dirs.append(n)

            if x == 0:
                init_dirs.append(e)
            elif x == len(lines[0]) - 1:
                init_dirs.append(w)

            for init_dir in init_dirs:
                best = max(best, simulate(init_pos, init_dir))
    # for y in range(len(lines)):
    for y in [0, Y]:
        for x in range(len(lines[0])):
            # for x in [0, X]:
            init_pos = (y, x)
            init_dirs = []
            if y == 0:
                init_dirs.append(s)
            elif y == len(lines) - 1:
                init_dirs.append(n)

            if x == 0:
                init_dirs.append(e)
            elif x == len(lines[0]) - 1:
                init_dirs.append(w)

            for init_dir in init_dirs:
                best = max(best, simulate(init_pos, init_dir))

    print(best)


def get_all_starts_chunked():
    # chunk_size = 2 * (X + Y) // cpu_count()
    chunks = [((y, 0), e) for y in range(Y)]
    chunks.extend([((y, X - 1), w) for y in range(0, Y)])
    chunks.extend([((0, x), s) for x in range(X)])
    chunks.extend([((Y - 1, x), n) for x in range(X)])

    def chunker_list(seq, size):
        return (seq[i::size] for i in range(size))

    def chunker_1(l, n):
        """Yield n number of striped chunks from l."""
        for i in range(0, n):
            yield l[i::n]

    return list(chunker_list(chunks, cpu_count() // 2))

    # left_right = product(range(0, Y), [0, X])
    # top_bot = product([0, Y], range(0, X))
    # return batched(chain(left_right, top_bot), cpu_count)


def solve_subsoln(starts):
    best = -1
    for start in starts:
        if start[0] == 0:
            best = max(best, simulate(start, s))
        elif start[0] == Y - 1:
            best = max(best, simulate(start, n))

        if start[1] == 0:
            best = max(best, simulate(start, e))
        elif start[1] == X - 1:
            best = max(best, simulate(start, w))

    return best


def solve_sub(starts):
    return max([simulate(s[0], s[1]) for s in starts])


if __name__ == '__main__':
    # iters = 1
    # x = timeit.timeit(lambda: f(), number=iters)
    # print(f"{x: 0.2f} s")

    start_chunks = get_all_starts_chunked()
    start = time.perf_counter()
    # with Pool() as p:
    #     print(max(p.map(solve_sub, start_chunks)))
    f()
    print((time.perf_counter() - start), " s")
