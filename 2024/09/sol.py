import timeit

with open('test.txt') as f:
    line = f.read().splitlines()[0]
    format = list(map(int, line))
    spread = []

    space = False
    next_id = 0
    for i in format:
        if space:
            spread += [""] * i
        else:
            spread += [next_id] * i
            next_id += 1
        space = not space
    # print(spread)


def f():
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
