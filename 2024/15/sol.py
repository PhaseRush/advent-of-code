import timeit

with open('test.txt') as f:
    lines = f.read().split("\n\n")
    grid = lines[0]
    grid = [list(row) for row in grid.split("\n")]
    Y = len(grid)
    X = len(grid[0])

    y = 0
    x = 0
    for i in range(Y):
        for j in range(X):
            if grid[i][j] == "@":
                y = i
                x = j
                break

    moves = lines[1].replace("\n","")
    print(moves, moves.find("\n"))

dirs = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0)
}

def p():
    print()
    for r in grid:
        print(*r)

def valid(y, x) -> bool:
    return 0 <= x < X and 0 <= y < Y and grid[y][x] != "#"


def move(pos, dir):
    y_0, x_0 = pos[0], pos[1]
    y_1, x_1 = y_0 + dir[0], x_0 + dir[1]

    if not valid(y_1, x_1):
        return pos

    boxes = []
    while grid[y_1][x_1] == "O":
        boxes.append((y_1, x_1))
        y_1, x_1 = y_1 + dir[0], x_1 + dir[1]

    if grid[y_1][x_1] == ".":  # end was not a wall
        grid[y_1][x_1], grid[y_0 + dir[0]][x_0 + dir[1]] = grid[y_0 + dir[0]][x_0 + dir[1]], grid[y_1][x_1]

    return y_1, x_1


def f():
    y_0 = y
    x_0 = x
    for m in moves:
        y_0, x_0 = move((y_0, x_0), dirs[m])
        p()

    s = 0
    for i in range(Y):
        for j in range(X):
            if grid[i][j] == "O":
                s += 100 * i + j
    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
