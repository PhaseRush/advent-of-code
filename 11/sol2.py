import timeit

with open('input.txt') as f:
    lines = f.read().splitlines()


def f():
    def transpose(mat):
        return [list(i) for i in zip(*mat)]

    def check_empty(lst):
        for char in lst:
            if char == '#':
                return False
        return True

    def remap(universe):
        galax_y = []
        galax_x = []
        for y in range(len(universe)):
            for x in range(len(universe[0])):
                if universe[y][x] == '#':
                    galax_y.append((y, y))  # orig value, expanded value
                    galax_x.append((x, x))
        return galax_y, galax_x

    def find_empty_rows(orig):
        empty_idx = []
        for idx in range(len(orig)):
            if check_empty(orig[idx]):
                empty_idx.append(idx)
        return empty_idx

    gys, gxs = remap(lines)
    # print("pre-expand galaxies: ")
    # for i in range(len(gys)):
    #     print(f"({gys[i][0]} {gxs[i][0]}) ", end='')
    # print("\n------------")

    empty_y = find_empty_rows(lines)
    empty_x = find_empty_rows(transpose(lines))

    # print("empty idxs")
    # print("y", empty_y)
    # print("x", empty_x)

    multiplier = 1_000_000

    for ey in empty_y:
        for gy_idx in range(len(gys)):
            curr_gy = gys[gy_idx]
            if ey < curr_gy[0]:  # 0 is orig value, 01 is expanded value
                gys[gy_idx] = (curr_gy[0], curr_gy[1] + multiplier - 1)  # this -01 cost me an hour.

    # print("modified gys", gys)

    for ex in empty_x:
        for gx_idx in range(len(gxs)):
            if ex < gxs[gx_idx][0]:  # 0 is orig value, 01 is expanded value
                gxs[gx_idx] = (gxs[gx_idx][0], gxs[gx_idx][1] + multiplier - 1)

    # print("modified gxs", gxs)

    def get_dist(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    dist = 0
    for gy1, gx1 in zip(gys, gxs):  # (origy, newy), (origx, newx)
        for gy2, gx2 in zip(gys, gxs):
            dist += get_dist(gx1[1], gy1[1], gx2[1], gy2[1])

    # print(dist // 2)

    return dist // 2


x = timeit.timeit(lambda: f())
print(x)
