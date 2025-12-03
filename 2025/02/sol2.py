import timeit
import os
import re

with open('2025/02/test.txt') as f:
    lines = f.read().splitlines()[0].split(",")
    pairs = [x.split("-") for x in lines]
    print(lines)


def f():
    pattern = re.compile(r"^(\d+)\1+$")
    ans = 0
    for a, b in pairs:
        for num in range(int(a), int(b) + 1):
            curr_num = str(num)
            if pattern.match(curr_num):
                ans += num
    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")

