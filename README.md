# Advent of Code 2023

[Advent of code](adventofcode.com) is a series of 25 daily coding challenges. They're pretty fun; check them out
sometime.

This repo contains my solutions to these problems. And this readme will summarize my thoughts for the day (this readme
was made on day 11, so I'm going by memory for earlier days).

I'll probably focus discussions on part 2 as those are typically the more interesting problems. But if part 1 is
interesting, I'll say something about it as well.

# 1 [3106/3732]

Easy one. Part 2 was pretty straight forward with a hardcoded digits string map.

I also saw an interesting soln which naively substituted all words with as such: `one` -> `one1one`. This way it
preserves the endpoints, as `one` and `eight` can be connected.

I had to spin this one up in a hurry, so I didn't do proper file i/o.

# 2 [2414/2915]

Not much to say, very simple with a count map

# 3 [6340/5084]

This one was a bit more challenging and annoying. I misunderstood the second part, thinking that a gear can have
multiple numbers as got a way larger answer.
Ended up just finding all the gears and brute forcing the 4 cardinal directions with index math.

# 4 [3732/9431]

Honestly these earlier days took longer to parse the input than to do the algo. This one was a simple little dp
propogation.

# 5 [5468/1360]

This one was all about parsing. Annoying and I ended up hardcoding th indices. My philosophy for the code here is to
produce the answer asap and not care about code quality nor style at all.

Sometimes I'll come back and fix up the code later but that's an afterthought, literally.

# 6 [3817/3648]

This one had a bunch of cool solutions, including this one I saw in desmos. Quite a simple problem, and easy to brute
force. That's another part of my philosophy: don't shy away from brute forcing a solution. Most of the time, it's faster
to just let it run than to think of then implement a better algo.

That being said: I've found that switching to pypy (3.12) instead of my normal python (3.10) does wonders, as it can
really optimize the loops which is what the brute force is crunching through anyways. Huge boost to performance, often
beating out my Java implementations.

# 7 [2987/4049]

Nice and clean soln by using a custom comparator. Was a huge fan of this problem. I saw a lot of people misread the
prompt by for example, using high card tie breaking.

# 8 [13077/7415]

Nice little LCM test. Parsing took half the time again honestly. Nice problem

# 9 [8056/7483]

Another nice math problem, simple to do pt2 as long as you clearly understand how your pt 1 worked.

# 10 [4501/1300]

The first hard problem. Part 1 was also quite difficult to parse through as there was a lot of setup I needed. Once I
had all the info set up, the algo was very easy as the loop is guaranteed so you just need to start it off.

Pt 2 was difficult. I thought of floodfill like many, but I didn't think of the technique to double the resolution to
account for adjacent walls. Ended up using the odd-parity trick which was easier to implement anyways.

# 11 [6402/7129]

Nice problem, was a fan of this one. Spent quite a while trying to rotate a matrix the right way as I thought it was
wrong. Turns out my printing was wrong :)))

Part 2 was fun. Code was messy as I had dis-coupled x and y but it was nice to do. I had an off-by-one errors with the
expansion factor, but it was easy once I debugged it.

Also today I saw someone get an u32 overflow. It's day 11 guys, cmon you have to learn by now.

Update: I was challenged to make an optimized version for part 2. I successfully dropped the runtime from about 50ms to
0.6ms, which you can find in the `sol2_2.py` file. Running it with python is about 20ms, and pypy drops it to 0.6ms.
Quite a good improvement, I'm happy with that as it's rivaling other people's "optimal" implementations in performance
langs.

# 12 [2512/652]

Meh recursive/dp problem. Annoying to code all the cases. Got my best ranking yet though, sub 1k. Today's goat was
@cache/@lru_cache. Orig sol was about 2s runtime, with multiprocessing, dropped it down to 250ms. Not bad. (Pypy slowed
this down at about 650ms)

# 13 [3775/2926]

Day 13 suffered with multithreading, which makes sense. Even though this is technically brute force, each pattern is
simply too small to justify the overhead. Problem itself was pretty simple but annoying. Meh problem.

# 14 [4850/4112]

Day 14 part 1 was really nice and intuitive. Part 2 was supposed to be a easy shift with a loop and cycle detection, but
I made a critical bug where my scoring function was refactored and I didn't find the issue for an hour. Costed me a good
chunk of time. However, the problem was not difficult and cycles were pretty obvious.

As a followup, I improved the naive shifting function by instead finding the cubes first, then shifting within a cube.
That reduces the characteristic quadratic down to linear. After profiling (pypy), dropped from 1.5s to 0.3s overall.

# 15 [3347/2688]

Day 15 was giga easy. Fell for the `[xxx] * 256` trick in python, costed me a few extra minutes. Caching the hash
function does improve performance by about 10% although the entire thing already runs sub ms

# 16 [2530/2076]

Pretty nice problem, nice and simple. Took me a while for part 1 but part 2 only an additional 4 minutes to brute force.

Tried a few optimizations, down to 130ms now. Multithreading needs to be more intelligent than per-start. I tried to use a total of #cpu chunked lists, but overhead is still too high.

# 17 [299/262]

Insane performance today. Was able to copy paste half the code from yesterday wrt reusing the visited bitmask. Familiar with dijistras and heapq meant this was my best performance yet.

# 18 [2603/999]

Not bad, pretty chill one. Had to pull out the numpy which meant no pypy today. 20s runtime. Not bad overall though, did learn about pick's theorem which is cool.

Reimplemented in Java (3.5-4s) for a class I'm involved in.