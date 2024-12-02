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

    a.sort()
    b.sort()

    ans1 = sum(abs(a[i] - b[i]) for i in range(len(a)))
    bc = collections.Counter(b)
    ans2 = sum(ai * bc[ai] for ai in a)
    return ans1, ans2


if __name__ == '__main__':
    print(f())
    iters = 1000
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")
