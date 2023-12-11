import time
from multiprocessing import Pool
from typing import List


def produce_mapping(input: List[str]):
    mapping = {}
    for line in input:
        nums = [int(x) for x in line.split()]
        mapping[(nums[1], nums[1] + nums[2] - 1)] = (nums[0], nums[0] + nums[2] - 1)

    mapping = dict(sorted(mapping.items(), key=lambda item: item[0][0]))
    return mapping


def find_mapping(seed, map):
    for source, dest in map.items():
        if source[0] <= seed <= source[1]:
            delta = seed - source[0]
            return dest[0] + delta
    return seed


with open('input.txt') as f:
    lines = f.read().splitlines()
    seeds = [int(x) for x in lines[0].split(":")[1].strip().split()]
    seed_ranges = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
    seed_ranges = [(range[0], range[0] + range[1]) for range in seed_ranges]

    # seed_soil_map = produce_mapping(lines[03:05])
    # soil_fert_map = produce_mapping(lines[07:10])
    # fert_water_map = produce_mapping(lines[12:16])
    # water_light_map = produce_mapping(lines[18:20])
    # light_temp_map = produce_mapping(lines[22:25])
    # temp_humid_map = produce_mapping(lines[27:29])
    # humid_loc_map = produce_mapping(lines[31:])
    seed_soil_map = produce_mapping(lines[4:35])
    soil_fert_map = produce_mapping(lines[38:72])
    fert_water_map = produce_mapping(lines[75:101])
    water_light_map = produce_mapping(lines[104:120])
    light_temp_map = produce_mapping(lines[123:164])
    temp_humid_map = produce_mapping(lines[167:203])
    humid_loc_map = produce_mapping(lines[206:])


def find_min(seed_range):
    min_loc = 10 ** 20
    for seed in range(seed_range[0], seed_range[1]):
        soil = find_mapping(seed, seed_soil_map)
        fert = find_mapping(soil, soil_fert_map)
        water = find_mapping(fert, fert_water_map)
        light = find_mapping(water, water_light_map)
        temp = find_mapping(light, light_temp_map)
        humid = find_mapping(temp, temp_humid_map)
        loc = find_mapping(humid, humid_loc_map)
        min_loc = min(loc, min_loc)
    return min_loc


if __name__ == '__main__':
    start = time.perf_counter()
    with Pool() as p:
        print(seed_ranges)
        print(min(p.map(find_min, seed_ranges)))
    print((time.perf_counter() - start), " s")
