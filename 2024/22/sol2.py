import timeit
from collections import deque, defaultdict

with open('input.txt') as f:
    lines = list(map(int, f.read().splitlines()))
    print(lines)


def next(n):
    n ^= (n * 64)
    n = n % 16777216
    n ^= int(n / 32)
    n = n % 16777216
    n ^= n * 2048
    n = n % 16777216
    return n


def f():
    s = 0
    bests = defaultdict(int)

    for curr_n in lines:
        cycle = deque()
        seen = set()

        for _ in range(2000):
            start = curr_n % 10
            curr_n = next(curr_n)
            end = curr_n % 10
            cycle.append((end, end - start))
            if len(cycle) > 4:
                cycle.popleft()

            cycle_hash = tuple(x[1] for x in cycle)
            if cycle_hash not in seen:
                seen.add(cycle_hash)
                if len(cycle) == 4:
                    bests[cycle_hash] += cycle[-1][0]

    s = max(bests.values())
    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
