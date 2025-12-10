import timeit
import itertools

with open("2025/09/test.txt") as f:
    lines = f.read().splitlines()
    coords = [tuple(map(int, x.split(","))) for x in lines]
    l = coords + [coords[0]]
    # lines = [list(row) for row in lines]
    # print(coords)


def check_intersect(x1, y1, x2, y2):
    for (lx1, ly1), (lx2, ly2) in itertools.pairwise(l):
        if not (
            max(lx1, lx2) <= min(x1, x2)
            or max(x1, x2) <= min(lx1, lx2)
            or max(ly1, ly2) <= min(y1, y2)
            or max(y1, y2) <= min(ly1, ly2)
        ):
            return False
    return True


def f():
    ans = 0
    max_coords = None
    for c1, c2 in itertools.combinations(coords, 2):
        x1, y1 = c1[0], c1[1]
        x2, y2 = c2[0], c2[1]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if check_intersect(x1, y1, x2, y2):
            ans = max(ans, area)

    print(f"ans {ans}")


if __name__ == "__main__":
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
