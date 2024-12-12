import timeit
import math
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


def iter(curr):
    new = []
    for n in curr:
        if n == 0:
            new.append(1)
        elif num_digits(n) % 2 == 0:
            a, b = split_num(n)
            new.append(a)
            new.append(b)
        else:
            new.append(n * 2024)

    return new





def f():
    res = nums
    for i in tqdm(range(25)):
        res = iter(res)
        print(i, len(res))
    print(len(res))
    return res

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
