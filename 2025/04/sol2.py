import timeit

with open('2025/04/test.txt') as f:
    lines = [list(x) for x in f.read().splitlines()]
    print(lines)
    Y = len(lines)
    X = len(lines[0])

dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def check_access(pos):
    y_0,x_0 = pos[0],pos[1]

    curr_check = 0
    for dy, dx in dirs:
        y_1, x_1 = y_0+dy, x_0+dx
        if not (0 <= y_1 < Y) or not (0 <= x_1 < X):
            continue

        if lines[y_1][x_1] == "@":
            curr_check += 1
    
    valid = curr_check < 4
    if valid:
        return True
    else:
        return False
        
def count_papers():
    return sum(map(lambda row: row.count("@"), lines))

def f():
    total_ans = 0
    papers = count_papers()

    while True:
        for y in range(Y):
            for x in range(X):
                if lines[y][x] == "@":
                    check = check_access((y, x))
                    if check:
                        lines[y][x] = "." # overwrite
                        total_ans += 1
        if papers == count_papers():
            break
        papers = count_papers()

    print(total_ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
