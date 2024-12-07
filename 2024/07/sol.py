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

            if int(str(candidate) + str(i)) <= t:
                next.append(int(str(candidate) + str(i)))
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
