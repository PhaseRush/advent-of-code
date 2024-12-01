import timeit

with open('input.txt') as f:
    patterns = []
    curr_pat = []
    for line in f.read().splitlines():
        if line == "":
            patterns.append(curr_pat.copy())
            curr_pat.clear()
        else:
            curr_pat.append(line)
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
            horizontals.append(i)  # short circuit?

    return horizontals


def f():
    ans = 0
    for pat in patterns:
        hors = check_hor(pat)
        vert = check_hor(rotate_matrix(pat))
        if len(vert) == 1:
            ans += vert[0]
        else:
            ans += hors[0] * 100
    print(ans)


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

