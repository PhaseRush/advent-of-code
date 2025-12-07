import timeit

with open('test.txt') as f:
    lines = f.read().splitlines()
    # lines = [list(row) for row in lines]


def f():
    pass


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
