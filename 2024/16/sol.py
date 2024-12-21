import timeit
import heapq
from collections import defaultdict

with open('input.txt') as f:
    lines = f.read().splitlines()

    grid = [list(r) for r in lines]
    print(grid)
    Y = len(grid)
    X = len(grid[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def start_end():
    for r, y in enumerate(lines):
        for c, char in enumerate(y):
            if char == "#":
                continue
            pos = (r, c)
            if char == "S":
                start = pos
            if char == "E":
                end = pos

    return start, end


def dij(starts):
    pq = []
    for y_0, x_0, dir in starts:
        heapq.heappush(pq, (0, y_0, x_0, dir))

    dist = defaultdict(lambda: 1_000_000)
    while pq:
        (d, row, col, direction) = heapq.heappop(pq)
        if dist[(row, col, direction)] < d:
            continue
        for next_dir in range(3):
            if next_dir == direction:
                continue
            if (row, col, next_dir) not in dist or dist[
                (row, col, next_dir)
            ] > d + 1000:
                dist[(row, col, next_dir)] = d + 1000
                heapq.heappush(pq, (d + 1000, row, col, next_dir))
        # print(direction)
        dr, dc = dirs[direction]
        next_row, next_col = row + dr, col + dc
        # print(next_row, next_col)
        if (
                0 <= next_row < len(grid)
                and 0 <= next_col < len(grid[0])
                and grid[next_row][next_col] != "#"
                and (
                (next_row, next_col, direction) not in dist
                or dist[(next_row, next_col, direction)] > d + 1
        )
        ):
            dist[(next_row, next_col, direction)] = d + 1
            heapq.heappush(pq, (d + 1, next_row, next_col, direction))

    return dist


def f():
    start, end = start_end()
    dist_start = dij([(start[0], start[1], 1)])

    optimal = 1_000_000
    for dir in range(3):
        if (end[0], end[1], dir) in dist_start:
            optimal = min(optimal, dist_start[(end[0], end[1], dir)])
    print("otp", optimal)

    dist_end = dij([(end[0], end[1], d) for d in range(3)])

    result = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for dir in range(3):
                state_from_start = (row, col, dir)
                state_from_end = (row, col, (dir + 2) % 4)
                if dist_start[state_from_start] + dist_end[state_from_end] == optimal:
                    result.add((row, col))

    print("res ", len(result))


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
