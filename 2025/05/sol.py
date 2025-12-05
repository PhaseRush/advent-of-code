import timeit

with open('2025/05/test.txt') as f:
    lines = f.read().splitlines()
    empty = lines.index("")
    fresh_ranges = [tuple(map(int, x.split("-"))) for x in lines[:empty]]
    fresh_ranges.sort(key=lambda pair: pair[0])
    spoiled = list(map(int, lines[empty+1:]))
    print(fresh_ranges, spoiled)

def f():
    ans = 0
    for check in spoiled:
        for low, high in fresh_ranges:
            if low <= check <= high:
                print(check)
                ans += 1
                break
    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
