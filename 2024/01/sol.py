import collections
import timeit

with open('input') as f:
    lines = f.read().splitlines()


def f():
    a = []
    b = []
    for l in lines:
        sp = l.split()
        a.append(int(sp[0]))
        b.append(int(sp[1]))

    bc = collections.Counter(b)
    ans = 0
    for p in a:
        ans += p * bc[p]
    return ans


if __name__ == '__main__':
    print(f())
    iters = 1000
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
