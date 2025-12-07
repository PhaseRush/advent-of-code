import timeit

with open('2025/07/test.txt') as f:
    lines = f.read().splitlines()
    # lines = [list(row) for row in lines]
    x_start = lines[0].index("S")
    # print(x_start)
    Y = len(lines)


def f():
    ans = 0
    curr_beam_x = [x_start]
    for y in range(1, Y):
        next_beam_x = set()
        for x in curr_beam_x:
            if lines[y][x] == ".":
                next_beam_x.add(x)
            else:
                next_beam_x.add(x-1)
                next_beam_x.add(x+1)
                ans += 1
        curr_beam_x = list(next_beam_x)
    
    print(ans)



if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
