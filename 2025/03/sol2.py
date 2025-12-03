import timeit
import itertools
from tqdm import tqdm

with open('2025/03/test.txt') as f:
    lines = f.read().splitlines()
    print(lines)

def get_best(num):
    digits = len(num)
    left_idx = 0
    ans = ""
    for idx in reversed(range(12)):
        curr_window = num[left_idx:digits-idx]
        max_digit = max(curr_window)
        new_left_idx = left_idx + curr_window.index(max_digit) + 1
        left_idx = new_left_idx
        ans += max_digit
    return int(ans)


def f():
    ans = 0
    for l in tqdm(lines):
        ans += get_best(l)
    
    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
