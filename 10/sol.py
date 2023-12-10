import itertools

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
    '7': [w, s],
    'F': [s, e],
    # '.': []
}

valid_chars = {
    n: ['|', '7', 'F'],
    e: ['-', 'J', '7'],
    s: ['|', 'J', 'L'],
    w: ['-', 'F', 'L']
}


def get_char(pos):
    return lines[pos[0]][pos[1]]


def get_next_pos(pos, dir):
    return pos[0] + dir[0], pos[1] + dir[1]


def find_next(curr_pos, from_pos=None):
    curr_valid_dirs = valid_dirs[curr_pos]
    for d in curr_valid_dirs:
        if from_pos != d:  # don't go backwards
            pass

    # try:
    # except:
    #     pass


def test(curr, goto):
    curr_char = get_char(curr)  # -
    next_pos = get_next_pos(curr, goto)  # (1, 3)
    next_char = get_char(next_pos)  # 7
    if next_char == 'S':
        return None, None
    from_dir = opposite[goto]  # w
    next_dir = valid_dirs[next_char].copy()  # [w, s]
    try:
        next_dir.remove(from_dir)  # [s]
    except:
        print("error", curr, curr_char, next_char, next_dir)
    # print(next_pos, next_dir[0])
    return next_pos, next_dir[0]


true_start = (54, 15)
start = (53, 15)

# true_start = (1, 1)
# start = (1, 2)
# print(get_char(start))
# print(get_char((53, 15)))


path = [start]
next = start
goto = n
# goto = e
while next:
    # try:
    next, goto = test(next, goto)
    if next:
        path.append(next)
        # print(next)
    # except:
    #     pass

path.insert(0, true_start)  # hardcode real start

# print(path)
print(path[len(path) // 2])
print('part a len', len(path) // 2)

path_set = set(path)

start_is_vert = True  # screw it just hard code

area = 0
area_incl = []
for y in range(len(lines)):
    odd_parity = False
    for x in range(len(lines[0])):
        if (y, x) in path_set:
            if lines[y][x] in "|JL" or (lines[y][x] == 'S' and start_is_vert):
                odd_parity = not odd_parity
        else:
            area += 1 if odd_parity else 0
            area_incl.append((x, y, get_char((x, y))))

print("area", area)
# print(area_incl)