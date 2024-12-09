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

Was a toposort problem, but I didn't feel like doing anything smart. Keep swapping until it's correct!
Ended up doing some cool benchmarking to determine that toposort would actually be substantially slower than the brute
force I took (in terms of runtime and impl time)

The interesting part is that pypy seemed to make both solutions slower.
Times are all in ms/iteration

| runtime \ algo | brute force | toposort (networkx) |
|----------------|-------------|---------------------|
| Python 3.12    | 1.8         | 20                  |
| pypy 3.13      | 200         | 40                  |

# Day 6: 2824/2166

pretty nice problem, just brute force it as per usual.

Played around with multiprocessing after the fact and brought the performance down quite nicely to about ~1-2 s.

# Day 7: 8219/6687

Second part just required a very small tweak to the first so it was fine. Nice and simple

# Day 8: 15921/14623

Started a bit late, this problem I thought would be more linalg focused but honestly just did it brute force since the
input space is so small (1.5ms)

# Day 9: 9877/6404 

Dumb bug on part 2, made a meh assumption and i had a bad conditional breakpoint so debugging was tough.


