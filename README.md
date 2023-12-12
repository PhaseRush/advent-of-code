# Advent of Code 2023

[Advent of code](adventofcode.com) is a series of 25 daily coding challenges. They're pretty fun; check them out
sometime.

This repo contains my solutions to these problems. And this readme will summarize my thoughts for the day (this readme was made on day 11, so I'm going by memory for earlier days).

I'll probably focus discussions on part 2 as those are typically the more interesting problems. But if part 1 is interesting, I'll say something about it as well.

# 1

Easy one. Part 2 was pretty straight forward with a hardcoded digits string map.

I also saw an interesting soln which naively substituted all words with as such: `one` -> `one1one`. This way it preserves the endpoints, as `one` and `eight` can be connected.

I had to spin this one up in a hurry, so I didn't do proper file i/o.

# 2

Not much to say, very simple with a count map

# 3

This one was a bit more challenging and annoying. I misunderstood the second part, thinking that a gear can have multiple numbers as got a way larger answer.
Ended up just finding all the gears and brute forcing the 4 cardinal directions with index math.


# 4
Honestly these earlier days took longer to parse the input than to do the algo. This one was a simple little dp propogation.

# 5

This one was all about parsing. Annoying and I ended up hardcoding th indices. My philosophy for the code here is to produce the answer asap and not care about code quality nor style at all.

Sometimes I'll come back and fix up the code later but that's an afterthought, literally.

# 6

This one had a bunch of cool solutions, including this one I saw in desmos. Quite a simple problem, and easy to brute force. That's another part of my philosophy: don't shy away from brute forcing a solution. Most of the time, it's faster to just let it run than to think of then implement a better algo.

That being said: I've found that switching to pypy (3.12) instead of my normal python (3.10) does wonders, as it can really optimize the loops which is what the brute force is crunching through anyways. Huge boost to performance, often beating out my Java implementations.

# 7

Nice and clean soln by using a custom comparator. Was a huge fan of this problem. I saw a lot of people misread the prompt by for example, using high card tie breaking.

# 8

Nice little LCM test. Parsing took half the time again honestly. Nice problem

# 9

Another nice math problem, simple to do pt2 as long as you clearly understand how your pt 1 worked.

# 10

The first hard problem. Part 1 was also quite difficult to parse through as there was a lot of setup I needed. Once I had all the info set up, the algo was very easy as the loop is guaranteed so you just need to start it off.

Pt 2 was difficult. I thought of floodfill like many, but I didn't think of the technique to double the resolution to account for adjacent walls. Ended up using the odd-parity trick which was easier to implement anyways.

# 11

Nice problem, was a fan of this one. Spent quite a while trying to rotate a matrix the right way as I thought it was wrong. Turns out my printing was wrong :)))

Part 2 was fun. Code was messy as I had dis-coupled x and y but it was nice to do. I had an off-by-one errors with the expansion factor, but it was easy once I debugged it.

Also today I saw someone get an u32 overflow. It's day 11 guys, cmon you have to learn by now.

Update: I was challenged to make an optimized version for part 2. I successfully dropped the runtime from about 50ms to 0.6ms, which you can find in the `sol2_2.py` file. Running it with python is about 20ms, and pypy drops it to 0.6ms. Quite a good improvement, I'm happy with that as it's rivaling other people's "optimal" implementations in performance langs.


# 12

Meh recursive/dp problem. Annoying to code all the cases. Got my best ranking yet though, sub 1k. Today's goat was @cache/@lru_cache. Orig sol was about 2s runtime, with multiprocessing, dropped it down to 250ms. Not bad. (Pypy slowed this down at about 650ms)
