from functools import cache
import timeit

with open('input.txt') as f:
    lines = f.read().splitlines()
    patterns = lines[0].split(", ")
    desired = lines[2:]
    print(desired)


@cache
def cons(pattern):
    if not pattern:
        return True  # finished cons
    count = 0
    count += sum(
        cons(pattern[len(test):])
        for test in patterns
        if pattern.startswith(test)
    )
    return count


def f():
    s = 0
    for d in desired:
        print(d)
        s += cons(d)

    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
