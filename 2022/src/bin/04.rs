pub fn part_one(input: &str) -> Option<u32> {
    let mut score = 0;

    for pair in input.split("\n") {
        let elves = pair.split(",").collect::<Vec<&str>>();
        let elf_1 = elves[0].split("-").collect::<Vec<&str>>();
        let elf_2 = elves[1].split("-").collect::<Vec<&str>>();
        let elf_1_start = elf_1[0].parse::<i32>().unwrap();
        let elf_1_end = elf_1[1].parse::<i32>().unwrap();
        let elf_2_start = elf_2[0].parse::<i32>().unwrap();
        let elf_2_end = elf_2[1].parse::<i32>().unwrap();

        if elf_1_start <= elf_2_start && elf_1_end >= elf_2_end {
            score += 1;
        } else if elf_1_start >= elf_2_start && elf_1_end <= elf_2_end {
            score += 1;
        }
    }

    return Some(score);
}

pub fn part_two(input: &str) -> Option<u32> {
    let mut score = 0;

    for pair in input.split("\n") {
        let elves = pair.split(",").collect::<Vec<&str>>();
        let elf_1 = elves[0].split("-").collect::<Vec<&str>>();
        let elf_2 = elves[1].split("-").collect::<Vec<&str>>();
        let elf_1_start = elf_1[0].parse::<i32>().unwrap();
        let elf_1_end = elf_1[1].parse::<i32>().unwrap();
        let elf_2_start = elf_2[0].parse::<i32>().unwrap();
        let elf_2_end = elf_2[1].parse::<i32>().unwrap();

        if !(elf_1_end < elf_2_start || elf_1_start > elf_2_end) {
            score += 1;
        }
    }

    return Some(score);
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 4);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 4);
        assert_eq!(part_one(&input), None);
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 4);
        assert_eq!(part_two(&input), None);
    }
}
