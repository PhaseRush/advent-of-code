with open('input.txt') as f:
    lines = f.read().splitlines()

n = (-1, 0)
e = (0, 1)
s = (1, 0)
w = (0, -1)

opposite = {
    n: s,
    s: n,
    e: w,
    w: e
}

dirs = [n, e, s, w]

valid_dirs = {
    '|': [n, s],
    '-': [e, w],
    'L': [n, e],
    'J': [n, w],
    '07': [w, s],
    'F': [s, e],
}


def get_char(pos):
    return lines[pos[0]][pos[1]]


def get_next_pos(pos, dir):
    return pos[0] + dir[0], pos[1] + dir[1]


def test(curr, goto):
    next_pos = get_next_pos(curr, goto)  # (01, 03)
    next_char = get_char(next_pos)  # 07
    if next_char == 'S':
        return None, None
    from_dir = opposite[goto]  # w
    next_dir = valid_dirs[next_char].copy()  # [w, s]
    next_dir.remove(from_dir)  # [s]

    return next_pos, next_dir[0]


true_start = (54, 15)
start = (53, 15)

path = [true_start, start]
next = start
goto = n
while next:
    next, goto = test(next, goto)
    if next:
        path.append(next)

print(path[len(path) // 2])
print(len(path) // 2)

path_set = set(path)
start_is_vert = True  # screw it just hard code

# apparently the optimal solution is to use the shoelace formula https://en.wikipedia.org/wiki/Shoelace_formula

area = 0
for y in range(len(lines)):
    odd_parity = False
    for x in range(len(lines[0])):
        if (y, x) in path_set:
            if lines[y][x] in "|JL" or (lines[y][x] == 'S' and start_is_vert):
                odd_parity = not odd_parity
        else:
            area += 1 if odd_parity else 0

print(area)
