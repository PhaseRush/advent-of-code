# Advent of Code 2024

Welcome to advent :)

# Day 1: 2788/2217

Fun first problem to get warmed up.

# Day 2: 10753/6824

Started a bit late, no stress.

# Day 3: 9934/8077

Started late again, still chill. Regex is a bit annoying - I think it can def be cleaned up with regex + py pattern
matching which I might do as a showcase

# Day 4: 67614/60536

Started during lunch the day after. Had to adjust solution between p1 and 2. I'm happy with my p2 solution since i didn'
t run into any bugs while implementing it. Still think I could've gone with my original idea with using a set of 3x3
convolutional kernels to scan through the grid, but this will do for today.

# Day 5: 6119/4007

Was a toposort problem but I didn't feel like doing anything smart. Keep swapping until it's correct!
Ended up doing some cool benchmarking to determine that toposort would actually be substantially slower than the brute
force I took (in terms of runtime and impl time)

The interesting part is that pypy seemed to make both solutions slower.
Times are all in ms/iteration

| runtime \ algo | brute force | toposort (networkx) |
|----------------|-------------|---------------------|
| Python 3.12    | 1.8         | 20                  |
| pypy 3.13      | 200         | 40                  |
