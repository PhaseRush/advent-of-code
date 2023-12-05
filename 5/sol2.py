from typing import List
from tqdm import tqdm

def produce_mapping(input: List[str]):
    mapping = {}
    for line in input:
        # print(line)
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
    seed_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
    print(seed_ranges)

    # seed_soil_map = produce_mapping(lines[3:5])
    # soil_fert_map = produce_mapping(lines[7:10])
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

    # print(seeds, seed_soil_map)
    min_loc = 10**20
    for seed_range in tqdm(seed_ranges):
        for seed in tqdm(range(seed_range[0], seed_range[1])):
    # for seed in seeds:
            soil = find_mapping(seed, seed_soil_map)
            # print(seed, soil)
            fert = find_mapping(soil, soil_fert_map)
            # print(seed, fert)
            water = find_mapping(fert, fert_water_map)
            # print(seed, water)
            light = find_mapping(water, water_light_map)
            # print(seed, light)
            temp = find_mapping(light, light_temp_map)
            # print(seed, temp)
            humid = find_mapping(temp, temp_humid_map)
            # print(seed, humid)
            loc = find_mapping(humid, humid_loc_map)
            # print(seed, loc)
            min_loc = min(loc, min_loc)

    print(min_loc)

