import timeit

with open('2025/09/test.txt') as f:
    lines = f.read().splitlines()
    coords = [tuple(map(int, x.split(","))) for x in lines]
    # lines = [list(row) for row in lines]
    print(coords)


def f():
    import itertools
    ans = 0
    max_coords = None
    for c1, c2 in itertools.combinations(coords, 2):
        x1, y1 = c1[0], c1[1]
        x2, y2 = c2[0], c2[1]
        area = (abs(x1-x2) + 1) * (abs(y1-y2) + 1)
        if area >= ans:
            ans = area
            max_coords = (c1, c2)
    print(ans, max_coords)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
