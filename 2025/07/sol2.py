from functools import cache
import timeit

with open('2025/07/test.txt') as f:
    lines = f.read().splitlines()
    # lines = [list(row) for row in lines]
    x_start = lines[0].index("S")
    Y = len(lines)

@cache
def helper(y, x):
    if y >= Y:
        return 1
    if lines[y][x] == "^":
        return helper(y+1, x-1) + helper(y+1, x+1)
    else:
        return helper(y+1, x)

def f():
    ans = helper(1, x_start)
    print(ans)



if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
