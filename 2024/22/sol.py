import timeit

with open('input.txt') as f:
    lines = list(map(int, f.read().splitlines()))
    print(lines)


def next(n):
    n ^= (n * 64)
    n = n % 16777216
    n ^= int(n / 32)
    n = n % 16777216
    n ^= n * 2048
    n = n % 16777216
    return n


def f():
    s = 0
    for curr_n in lines:
        for _ in range(2000):
            curr_n = next(curr_n)
        s += curr_n

    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
