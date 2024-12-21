import timeit


def p():
    print()
    for r in grid:
        print(*r)


with open('input.txt') as f:
    lines = f.read().split("\n\n")
    grid = lines[0]
    initial_grid = [list(row) for row in grid.split("\n")]
    Y = len(grid)
    X = len(grid[0])

    y = 0
    x = 0
    grid = []
    for row in range(len(initial_grid)):
        if len(grid) <= row or row not in grid:
            grid.append([])

        for col in range(len(initial_grid[0])):
            # print(initial_grid[row][col])
            match initial_grid[row][col]:
                case "#":
                    grid[row].extend(["#", "#"])
                case "O":
                    grid[row].extend(["[", "]"])
                case ".":
                    grid[row].extend([".", "."])
                case "@":
                    grid[row].extend(["@", "."])

    Y = len(grid)
    X = len(grid[0])
    p()
    for i in range(Y):
        for j in range(X):
            if grid[i][j] == "@":
                y = i
                x = j
                break

    moves = lines[1].replace("\n", "")
    print(moves, moves.find("\n"))

dirs = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0)
}


def valid(y, x):
    return 0 <= x < X and 0 <= y < Y and grid[y][x] != "#"


def test(y_0, x_0, dy, dx, visited):
    if (y_0, x_0) in visited:
        return True
    visited.add((y_0, x_0))

    nr, nc = y_0 + dy, x_0 + dx
    match grid[nr][nc]:
        case "#":
            return False
        case "[":
            return test(nr, nc, dy, dx, visited) and \
                test(nr, nc + 1, dy, dx, visited)
        case "]":
            return test(nr, nc, dy, dx, visited) and \
                test(nr, nc - 1, dy, dx, visited)
        case "O":
            return test(nr, nc, dy, dx, visited)
    return True


def move(y_0, x_0, delta):
    dy = delta[0]
    dx = delta[1]
    y_1, x_1 = y_0 + dy, x_0 + dx

    if not valid(y_1, x_1):
        return y_0, x_0

    if grid[y_1][x_1] in "[]":
        visited = set()

        if not test(y_0, x_0, dy, dx, visited):
            return y_0, x_0

        while visited:
            for y_test, x_test in visited.copy():
                y_test_1, x_test_1 = y_test + dy, x_test + dx
                if (y_test_1, x_test_1) not in visited:
                    if grid[y_test_1][x_test_1] != "@" and grid[y_test][x_test] != "@":
                        grid[y_test_1][x_test_1] = grid[y_test][x_test]
                        grid[y_test][x_test] = "."

                    visited.remove((y_test, x_test))

    grid[y_0][x_0], grid[y_1][x_1] = grid[y_1][x_1], grid[y_0][x_0]
    return y_1, x_1


def f():
    y_0 = y
    x_0 = x
    for m in moves:
        y_0, x_0 = move(y_0, x_0, dirs[m])
        # p()

    s = 0
    for i in range(Y):
        for j in range(X):
            if grid[i][j] == "[":
                s += 100 * i + j
    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
