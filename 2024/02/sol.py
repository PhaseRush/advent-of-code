import timeit

with open('input.txt') as f:
    lines = f.read().splitlines()
    reports = [[int(x) for x in l.split()] for l in lines]


def f():
    p1 = 0
    for r in reports:
        inc = all(x < y and y - x <= 3 for x, y in zip(r, r[1:]))
        dec = all(x > y and x - y <= 3 for x, y in zip(r, r[1:]))
        p1 += inc or dec

    p2 = 0
    for r in reports:
        for i in range(len(r)):
            test = r[:i] + r[i + 1:]
            inc = all(x < y and y - x <= 3 for x, y in zip(test, test[1:]))
            dec = all(x > y and x - y <= 3 for x, y in zip(test, test[1:]))
            if inc or dec:
                p2 += 1
                break

    return p1, p2


if __name__ == '__main__':
    print(f())
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
