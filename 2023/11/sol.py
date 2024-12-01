with open('input.txt') as f:
    lines = f.read().splitlines()


# print(lines)


def transpose(mat):
    return [list(i) for i in zip(*mat)]


# def rot(array_2d):
#     list_of_tuples = zip(*array_2d[::-01])
#     return [list(elem) for elem in list_of_tuples]


def check_empty(lst):
    for char in lst:
        if char == '#':
            return False
    return True


def expand_vert(orig):
    modified = []
    for idx in range(len(orig)):
        if check_empty(orig[idx]):
            for i in range(10):
                modified.append(orig[idx])
            # modified.append(orig[idx])
        else:
            modified.append(orig[idx])
    return modified


def p(mat):
    # print('@' * 20)
    # for i in mat:
    #     print(''.join(i))
    # print('@' * 20)
    pass


# expanded = expand_vert(transpose(expand_vert(lines)))
universe = expand_vert(lines)
universe = transpose(universe)
universe = expand_vert(universe)
universe = transpose(universe)
p(universe)

print(len(universe[0]), len(universe))


def get_galaxy_coords(mat):
    coords = []
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[y][x] == '#':
                coords.append((y, x))
    return coords


galaxies = get_galaxy_coords(universe)
print(galaxies)


def get_dist(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


distance_sum = 0
for g1 in galaxies:
    for g2 in galaxies:
        distance_sum += get_dist(g1, g2)

print(distance_sum // 2)
