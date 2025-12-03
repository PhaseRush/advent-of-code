import timeit
import itertools
from tqdm import tqdm

with open('2025/03/test.txt') as f:
    lines = f.read().splitlines()
    print(lines)


def f():
    ans = 0

    for l in tqdm(lines):
        curr_ans = 0
        for comb in itertools.combinations(l, 2):
            val = int(comb[0] + comb[1])
            curr_ans = max(curr_ans, val)
        ans += curr_ans
    
    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
