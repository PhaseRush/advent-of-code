use std::cmp;
use std::collections::BinaryHeap;

pub fn part_one(input: &str) -> Option<u32> {
    let array = input.split("\n\n");
    let mut max = 0;
    for elf in array {
        let mut elf_sum = 0;
        let calories = elf.split("\n");
        for cal in calories {
            elf_sum += cal.parse::<u32>().unwrap();
        }
        max = cmp::max(max, elf_sum);
    }
    return Some(max);
}

pub fn part_two(input: &str) -> Option<u32> {
    let mut heap = BinaryHeap::new();
    let array = input.split("\n\n");
    for elf in array {
        let mut elf_sum = 0;
        let calories = elf.split("\n");
        for cal in calories {
            elf_sum += cal.parse::<u32>().unwrap();
        }
        heap.push(elf_sum);
    }

    return Some(heap.pop().unwrap() + heap.pop().unwrap() + heap.pop().unwrap());
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 1);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 1);
        assert_eq!(part_one(&input), None);
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 1);
        assert_eq!(part_two(&input), None);
    }
}
