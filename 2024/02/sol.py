import timeit

with open('input') as f:
    lines = f.read().splitlines()


def f():
    pass


print(lines)

if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
