import timeit

with open('input.txt') as f:
    lines = f.read().splitlines()


def f():
    has_x = set()
    has_y = set()
    galaxies = []

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == '#':
                has_y.add(y)
                has_x.add(x)
                galaxies.append((y, x))

    empty_y = [0] * len(lines)
    empty_x = [0] * len(lines[0])

    for y in range(len(lines)):
        if y in has_y:
            empty_y[y] = empty_y[y - 1] or 0
        else:
            empty_y[y] = empty_y[y - 1] + 1

    for x in range(len(lines[0])):
        if x in has_x:
            empty_x[x] = empty_x[x - 1] or 0
        else:
            empty_x[x] = empty_x[x - 1] + 1

    multiple = 1_000_000 - 1

    def dist(g1, g2):
        g1_y = g1[0] + empty_y[g1[0]] * multiple
        g2_y = g2[0] + empty_y[g2[0]] * multiple

        g1_x = g1[1] + empty_x[g1[1]] * multiple
        g2_x = g2[1] + empty_x[g2[1]] * multiple

        return abs(g2_y - g1_y) + abs(g2_x - g1_x)

    dist_sum = 0
    for g1 in range(len(galaxies)):
        for g2 in range(g1 + 1, len(galaxies)):
            dist_sum += dist(galaxies[g1], galaxies[g2])

    # print(dist_sum)
    return dist_sum


f()

iters = 1000
x = timeit.timeit(lambda: f(), number=iters)
print(f"{x: 0.2f} ms")
