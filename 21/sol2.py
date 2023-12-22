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
    orig_y = pos[0]
    orig_x = pos[1]

    y = pos[0] % Y #if pos[0] > 0 else -(abs(pos[0]) % Y)
    x = pos[1] % X #if pos[1] > 0 else -(abs(pos[1]) % X)
    neighbours = set()
    try:
        if lines[y][x - 1] != '#':
            neighbours.add((orig_y, orig_x - 1))
    except:
        pass
    try:
        if lines[y][x + 1] != '#':
            neighbours.add((orig_y, orig_x + 1))
    except:
        pass
    try:
        if lines[y - 1][x] != '#':
            neighbours.add((orig_y - 1, orig_x))
    except:
        pass
    try:
        if lines[y + 1][x] != '#':
            neighbours.add((orig_y + 1, orig_x))
    except:
        pass
    return neighbours


def calc(max_steps):
    q = deque([(0, start_pos)])

    visited = {(0, start_pos)}

    while q:
        step_count, curr_pos = q.popleft()
        if step_count == max_steps + 1:
            break
        neighbours = get_neighbours(curr_pos)  # - visited
        # stepped_neighbours = set()
        # for n in neighbours:
        #     stepped_neighbours.add(step_count, n)

        # stepped_neighbours -= visited
        # q.extend([(step_count + 1, neighbour) for neighbour in neighbours])
        for n in neighbours:
            next = (step_count + 1, n)
            if next not in visited:
                q.append(next)
                visited.add(next)
            # q.append((step_count + 1, n))
            # visited.add((step_count + 1, n))

    # print(f"{len(visited)=}, {visited=}")

    count = 0
    for step, pos in visited:
        if step == max_steps:
            count += 1
            # print(pos)

    print(count)
    return count


# print(lines)

zeros = [3759, 33496, 92857]


def f(n):
    b0 = zeros[0]
    b1 = zeros[1] - zeros[0]
    b2 = zeros[2] - zeros[1]
    return b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)


print(f(26501365 // X))

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(26501365 // X), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
