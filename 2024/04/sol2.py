import collections
import timeit

with open('input.txt') as f:
    lines = f.read().splitlines()
    Y = len(lines)
    X = len(lines[0])
    cmap = {(y, x): c for y, row in enumerate(lines) for x, c in enumerate(row)}
    cmap = collections.defaultdict(lambda: "", cmap)


def f():
    count = 0
    offsets = [-1, 0, 1]
    patterns = [['M', 'A', 'S'], ['S', 'A', 'M']]
    for y in range(Y):
        for x in range(X):
            first = [cmap[(y + d, x + d)] for d in offsets]
            second = [cmap[(y - d, x + d)] for d in offsets]  # rot 90
            count += first in patterns and second in patterns

    print(count)
    return count


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
