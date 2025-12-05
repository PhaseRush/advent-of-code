import timeit
from tqdm import tqdm

with open('2025/05/test.txt') as f:
    lines = f.read().splitlines()
    empty = lines.index("")
    fresh_ranges = [tuple(map(int, x.split("-"))) for x in lines[:empty]]
    fresh_ranges.sort(key=lambda pair: pair[0])
    spoiled = list(map(int, lines[empty+1:]))
    print(fresh_ranges, spoiled)

def f():
    ans = fresh_ranges[0][1] - fresh_ranges[0][0] + 1
    prev_high = fresh_ranges[0][1]
    print(f"starting ans {ans}")
    for curr_low, curr_high in tqdm(fresh_ranges[1:]):
        curr_low = max(curr_low, prev_high + 1)
        if curr_low > curr_high:
            continue
        
        curr_addition = curr_high - curr_low + 1
        
        ans += curr_addition
        prev_high = curr_high
    
        print(f"curr_add {curr_addition}")
    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
