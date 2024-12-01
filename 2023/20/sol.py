import functools
import math
import timeit
from collections import defaultdict, deque

with open('input.txt') as f:
    lines = f.read().splitlines()

    modules = {}
    for l in lines:
        module, destinations = l.split(" -> ")
        destinations = destinations.split(', ')
        if module == "broadcaster":
            module_type = None
        else:
            module_type = module[0]
            module = module[1:]
        modules[module] = (module_type, destinations)

    state = {}
    wires = defaultdict(list)

    for module, (type, destinations) in modules.items():
        for d in destinations:
            wires[d].append(module)

    for module, (type, destinations) in modules.items():
        if type == '%':
            state[module] = False
        elif type == '&':
            state[module] = {
                d: False for d in wires[module]
            }


def f():
    rx = wires['rx'][0]
    sources = wires[rx]
    # print(sources)  # ['bt', 'dl', 'fr', 'rv']

    cycles = {}

    cycle = 0
    while True:
        cycle += 1
        todo = deque([(None, 'broadcaster', False)])
        while todo:
            next_timestep = deque()

            for from_module, curr_module, high_pulse in todo:
                # pt2
                if curr_module in sources and not high_pulse:
                    if curr_module not in cycles:
                        cycles[curr_module] = cycle
                        if len(cycles) == len(sources):  # should be 4
                            # print(cycles)
                            print(functools.reduce(math.lcm, cycles.values()), " should be 225386464601017")
                            # return functools.reduce(math.lcm, cycles.values())
                            return

                curr_details = modules.get(curr_module)
                if not curr_details:
                    continue

                type, dests = curr_details
                if type == '%' and not high_pulse:
                    pulse_state = state[curr_module]
                    state[curr_module] = not pulse_state
                    next_timestep.extend([(curr_module, dest, not pulse_state) for dest in dests])
                elif type == '&':
                    pulse_state = state[curr_module]
                    pulse_state[from_module] = high_pulse
                    to_send = not all(pulse_state.values())
                    next_timestep.extend([(curr_module, dest, to_send) for dest in dests])
                elif type is None:
                    next_timestep.extend([(curr_module, dest, high_pulse) for dest in dests])
            todo = next_timestep

    # print(f"{lows=}, {highs=}, {lows*highs=}")


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x: 0.2f} s")

# print(sum(totals))
