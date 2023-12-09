import time

with open('input.txt') as f:
    lines = f.read().splitlines()

    start = time.process_time_ns()


    def derive(seq):
        # check all zero

        dx = [0] * (len(seq) - 1)
        # same = True
        all_zeros = True
        for i in range(len(seq) - 1):
            dx[i] = seq[i + 1] - seq[i]
            if dx[i] != 0:
                all_zeros = False

        if all_zeros:
            return seq[-1] + dx[0]
        else:
            return seq[-1] + derive(dx)


    nexts = []

    for line in lines:
        nums = [int(x) for x in line.split()]
        nexts.append(derive(nums))

    print(nexts)
    print(sum(nexts))

    print((time.process_time_ns() - start) / 10e6, " ms")
