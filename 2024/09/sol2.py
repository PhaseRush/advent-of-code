import collections
import timeit

with open('input.txt') as f:
    line = f.read().splitlines()[0]
    format = list(map(int, line))
    spread = []
    id_locs = {}  # id -> (start idx in spread, length of this id)
    gap_locs = collections.defaultdict(list)  # length -> start, impl sorted by idx

    space = False
    next_id = 0
    for i in format:
        if space:
            gap_locs[i].append(len(spread))
            spread += [""] * i

        else:
            id_locs[next_id] = (len(spread), i)
            spread += [next_id] * i
            next_id += 1
        space = not space
    # print(spread)
    print(id_locs)
    # print()

    # print(gap_locs)


def f():
    for i in sorted(id_locs.keys(), reverse=True):
        this_start, this_len = id_locs[i]
        # print(i)
        gap_candidates = [(gap_len, gap_idxs[0]) for gap_len, gap_idxs in gap_locs.items() if
                          gap_len >= this_len and gap_idxs]
        gap_candidates.sort(key=lambda x: x[1])  # sort by earliest index
        if not gap_candidates:
            continue

        gap_len, gap_start = gap_candidates[0]
        if this_start <= gap_start:
            continue

        id_locs[i] = (gap_start, this_len)  # write file to gap

        # update gaps
        rem_gap_len = gap_len - this_len
        # if rem_gap_len:
        rem_gap_idx = gap_start + this_len

        del gap_locs[gap_len][0]
        gap_locs[rem_gap_len].append(rem_gap_idx)
        gap_locs[rem_gap_len].sort()  # this was my bug :(

    # re-build spread?
    new_spread = ["."] * len(spread)
    for id, (id_idx, id_len) in id_locs.items():
        for i in range(id_idx, id_idx + id_len):
            new_spread[i] = id

    print(gap_locs)
    print(new_spread)

    ###
    s = 0
    print(id_locs)
    for id, (id_idx, id_len) in id_locs.items():
        for i in range(id_idx, id_idx + id_len):
            s += id * i
    print(s)
    return s


def f2():
    last_idx = len(spread) - 1
    for idx in range(len(spread)):
        # print(idx, last_idx)
        if idx >= last_idx:
            break
        if spread[idx] == "":
            # swap last idx
            while spread[last_idx] == "":
                last_idx -= 1
            if last_idx <= idx:
                break
            spread[idx] = spread[last_idx]
            spread[last_idx] = ""
            last_idx -= 1
        if spread[idx] == "":
            print("invalid, ", i)
        # print(i, spread)

    print("\n\n")
    print(spread)
    s = 0
    for idx in range(len(spread)):
        if spread[idx] == "":
            break
        s += idx * spread[idx]

    print(s)
    return s


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
