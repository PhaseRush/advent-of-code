import timeit
from collections import deque

with open('input.txt') as f:
    lines = f.read().splitlines()

n = (-1, 0)
e = (0, 1)
s = (1, 0)
w = (0, -1)


def move(pos, dir):
    return pos[0] + dir[0], pos[1] + dir[1]


def dir_index(dir):
    if dir == n:
        return 0
    elif dir == e:
        return 1
    elif dir == s:
        return 2
    else:
        return 3


choice = {
    '.': [[n], [e], [s], [w]],
    '/': [[e], [n], [w], [s]],
    '\\': [[w], [s], [e], [n]],
    '|': [[n], [n, s], [s], [n, s]],
    '-': [[e, w], [e], [e, w], [w]]
}


def get(pos):
    if pos[0] < 0 or pos[0] >= len(lines) or pos[1] < 0 or pos[1] >= len(lines[0]):
        return None
    return lines[pos[0]][pos[1]]


def simulate(init_pos, init_dir):
    visited = set()
    unique_pos = set()

    q = deque([(init_pos, init_dir)])
    while q:
        pos, dir = q.popleft()
        curr_char = get(pos)
        if not curr_char:
            continue

        if (pos, dir) not in visited:
            visited.add((pos, dir))
            unique_pos.add(pos)
            new_dirs = choice[curr_char][dir_index(dir)]
            for new_dir in new_dirs:
                q.append((move(pos, new_dir), new_dir))

    return len(unique_pos)


def f():
    best = -1
    for y in range(len(lines)):
        for x in range(len(lines[0])):
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


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
