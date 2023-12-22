import timeit

with open('input.txt') as f:
    lines = [line.split('~') for line in f.read().splitlines()]
    bricks = []
    for start, end in lines:
        start = tuple(map(int, start.split(',')))
        end = tuple(map(int, end.split(',')))
        cubes = {start, end}
        for i in range(2):
            if start[i] != end[i]:
                for j in range(min(start[i], end[i]) + 1, max(start[i], end[i])):
                    curr = list(start)
                    curr[i] = j
                    cubes.add(tuple(curr))
        bricks.append(cubes)
    bricks.sort(key=lambda cubes: min(cube[2] for cube in cubes))

N = len(bricks)


def simulate(bricks):
    settled = set()
    result = []
    num_fell = 0
    for cubes in bricks:
        shifted = False
        can_move = True
        while can_move:
            new_cubes = [(x, y, z - 1) for x, y, z in cubes]
            if all((cube[2] != 0 and (cube not in settled)) for cube in new_cubes):
                cubes = new_cubes
                shifted = True
            else:
                break

        settled.update(cubes)
        result.append(cubes)
        num_fell += shifted

    return result, num_fell


def f():
    result, _ = simulate(bricks)
    p1 = 0
    p2 = 0

    for disintegrate_idx in range(N):
        disintegrated = result.copy()
        disintegrated.pop(disintegrate_idx)
        _, num_fell = simulate(disintegrated)
        if num_fell == 0:
            p1 += 1
        else:
            p2 += num_fell

    print(p1, p2)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
