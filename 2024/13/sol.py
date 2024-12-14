import timeit
import itertools
import re

with open('input.txt') as f:
    lines = f.read().splitlines()
    machines = list(itertools.batched(lines, 4))  # incl newline
    print(machines)
    parsed = []
    for a in machines:
        match_A = re.search(r".*X\+(\d+).*Y\+(\d+)", a[0])
        dxa = int(match_A.group(1))
        dya = int(match_A.group(2))

        match_B = re.search(r".*X\+(\d+).*Y\+(\d+)", a[1])
        dxb = int(match_B.group(1))
        dyb = int(match_B.group(2))

        match_prize = re.search(r".*X=(\d+).*Y=(\d+)", a[2])
        xprize = int(match_prize.group(1)) + 10000000000000
        yprize = int(match_prize.group(2)) + 10000000000000
        parsed.append((dxa, dya, dxb, dyb, xprize, yprize))


def solve(m):
    dxa = m[0]
    dya = m[1]
    dxb = m[2]
    dyb = m[3]
    xprize = m[4]
    yprize = m[5]

    b = (xprize * dya - yprize * dxa) // (dya * dxb - dyb * dxa)
    a = (xprize * dyb - yprize * dxb) // (dyb * dxa - dxb * dya)

    if a * dxa + b * dxb == xprize and a * dya + b * dyb == yprize:
        return a * 3 + b

    return 0


def f():
    s = sum(solve(m) for m in parsed)
    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
