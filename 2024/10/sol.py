import collections
import timeit

with open('input.txt') as f:
    lines = f.read().splitlines()
    grid = [[int(x) if x.isdigit() else x for x in list(l)] for l in lines]
    print(grid)
    Y = len(grid)
    X = len(grid[0])
    heads = []
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 0:
                heads.append((y, x))
    print(heads)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def traverse_head(head):
    q = collections.deque()
    q.append(head)
    tails = set()
    while q:
        curry, currx = q.popleft()
        curr_val = grid[curry][currx]
        print("iter, ", q)
        if curr_val == 9:
            tails.add((curry, currx))
            continue

        for dy, dx in dirs:
            nexty, nextx = curry + dy, currx + dx
            if nexty in range(Y) and nextx in range(X):
                next_val = grid[nexty][nextx]
                if next_val == ".":
                    continue
                if grid[nexty][nextx] == curr_val + 1:
                    q.append((nexty, nextx))


    return len(tails)

def f():
    count = 0
    for head in heads:
        count += traverse_head(head)

    print(count)
    return count


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
