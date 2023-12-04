from collections import defaultdict

with open('input.txt') as f:
    total = defaultdict(int)
    count = [1] * 209
    for idx, line in enumerate(f):
        game, nums = line.strip().split(":")
        winners, sample = nums.strip().split("|")
        winners = winners.strip().split()
        sample = sample.strip().split()

        num_intersections = len(set(winners).intersection(set(sample)))

        for update in range(num_intersections):
            count[idx + 1 + update] += count[idx]

    print(sum(count))