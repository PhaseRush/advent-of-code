import timeit
from collections import deque

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

with open('input.txt') as f:
    lines = [list(line) for line in f.read().splitlines()]
    start_pos = (0, 0)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':
                start_pos = (y, x)

Y = len(lines)
X = len(lines[0])


def get_neighbours(pos):
    y = pos[0]
    x = pos[1]
    neighbours = set()
    if x > 0 and lines[y][x - 1] != '#':
        neighbours.add((y, x - 1))
    if x + 1 < X and lines[y][x + 1] != '#':
        neighbours.add((y, x + 1))
    if y > 0 and lines[y - 1][x] != '#':
        neighbours.add((y - 1, x))
    if y + 1 < Y and lines[y + 1][x] != '#':
        neighbours.add((y + 1, x))
    return neighbours


def f():
    q = deque([(0, start_pos)])

    visited = {(0, start_pos)}

    max_steps = 64
    while q:
        step_count, curr_pos = q.popleft()
        if step_count == max_steps + 1:
            break
        neighbours = get_neighbours(curr_pos)  # - visited

        for n in neighbours:
            next = (step_count + 1, n)
            if next not in visited:
                q.append(next)
                visited.add(next)


    print(f"{len(visited)=}, {visited=}")

    count = 0
    for step, pos in visited:
        if step == max_steps:
            count += 1

    print(count)

print(lines)

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
