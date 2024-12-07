import collections
import timeit

with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)
    eqs = []

    for l in lines:
        target, nums = l.split(": ")
        eqs.append((int(target), list(map(int, nums.split()))))
    # print(eqs)


def nbdigit(x):  # https://stackoverflow.com/a/61889467
    if x >= 10000000000000000:  # 17 -
        return len(str(x))
    if x < 100000000:  # 1 - 8
        if x < 10000:  # 1 - 4
            if x < 100:
                return (x >= 10) + 1
            else:
                return (x >= 1000) + 3
        else:  # 5 - 8
            if x < 1000000:
                return (x >= 100000) + 5
            else:
                return (x >= 10000000) + 7
    else:  # 9 - 16
        if x < 1000000000000:  # 9 - 12
            if x < 10000000000:
                return (x >= 1000000000) + 9
            else:
                return (x >= 100000000000) + 11
        else:  # 13 - 16
            if x < 100000000000000:
                return (x >= 10000000000000) + 13
            else:
                return (x >= 1000000000000000) + 15


def concat(a, b):
    a = a * 10**nbdigit(b)
    return a + b


def solve(t, nums):
    start = [nums[0]]
    next = []
    curr_idx = 1
    for i in nums[curr_idx:]:
        curr_idx += 1
        for candidate in start:
            if candidate + i <= t:
                next.append(candidate + i)
            if candidate * i <= t:
                next.append(candidate * i)

            c = concat(candidate, i)
            if c <= t:
                next.append(c)
        start = next
        next = []
    for n in start:
        if n == t:
            return True
    return False


def f():
    s = 0
    for t, nums in eqs:
        s += t if solve(t, nums) else 0
    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
