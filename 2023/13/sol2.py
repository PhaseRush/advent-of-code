import timeit

with open('input.txt') as f:
    patterns = []
    curr_pat = []
    for line in f.read().splitlines():
        if line == "":
            patterns.append(curr_pat.copy())
            curr_pat.clear()
        else:
            curr_pat.append(list(line))
    patterns.append(curr_pat)


def transpose(mat):
    return [list(i) for i in zip(*mat)]


def rotate_matrix(m):
    return [list(reversed(col)) for col in zip(*m)]


def check_hor(pattern):
    horizontals = []
    for i in range(1, len(pattern)):
        below = []
        above = []
        for j in range(i, len(pattern)):
            below.append(pattern[j])
        for j in reversed(range(0, i)):
            above.append(pattern[j])
        num_matching = min(len(above), len(below))
        above = above[:num_matching]
        below = below[:num_matching]
        if above == below:
            horizontals.append(i)

    return horizontals


def fix(pat):
    hors = check_hor(pat)
    vert = check_hor(rotate_matrix(pat))
    for y in range(len(pat)):
        for x in range(len(pat[0])):
            pat[y][x] = '.' if pat[y][x] == '#' else '#'
            fix_hors = check_hor(pat)
            fix_vert = check_hor(rotate_matrix(pat))
            fix_hors = list(set(fix_hors) - set(hors))
            fix_vert = list(set(fix_vert) - set(vert))

            if len(fix_hors) + len(fix_vert) == 1:
                return fix_hors[0] if fix_hors else 0, fix_vert[0] if fix_vert else 0

            pat[y][x] = '.' if pat[y][x] == '#' else '#'


def f():
    ans = 0
    for pat in patterns:
        hors, vert = fix(pat)
        ans += vert + 100 * hors
    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.4f} ms")
