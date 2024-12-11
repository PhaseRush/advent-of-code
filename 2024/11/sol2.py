import timeit
import math
from functools import lru_cache

from tqdm import tqdm

with open('input.txt') as f:
    lines = f.read().splitlines()
    nums = [int(x) for x in lines[0].split()]


def num_digits(n):
    return int(math.log10(n)) + 1


def split_num(n):
    s = str(n)
    half = len(s) // 2
    return int(s[:half]), int(s[half:])


@lru_cache(None)
def iter(n, iters):
    if not iters:
        return 1
    elif n == 0:
        return iter(1, iters - 1)
    elif num_digits(n) % 2 == 0:
        a, b = split_num(n)
        return iter(a, iters - 1) + iter(b, iters - 1)
    else:
        return iter(n * 2024, iters - 1)


def f():
    s = sum(iter(n, 75) for n in nums)
    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
