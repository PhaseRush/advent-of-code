use std::collections::HashSet;

pub fn part_one(input: &str) -> Option<u32> {
    let mut score = 0;

    for rucksack in input.split("\n") {
        let first = &rucksack[0..rucksack.len() / 2];
        let second = &rucksack[rucksack.len() / 2..rucksack.len()];
        let first_set: HashSet<char> = first.chars().into_iter().collect();
        let second_set: HashSet<char> = second.chars().into_iter().collect();
        let all_set: HashSet<char> = rucksack.chars().into_iter().collect();
        let mut duplicate = '0';
        for item in all_set {
            if first_set.contains(&item) && second_set.contains(&item) {
                duplicate = item;
                break;
            }
        }
        if duplicate as u32 >= 97 {
            score += duplicate as u32 - 96
        } else {
            score += duplicate as u32 - 38
        }
    }

    return Some(score as u32);
}

pub fn part_two(input: &str) -> Option<u32> {
    let mut score = 0;

    for triple in input.split("\n").map(str::to_string).collect::<Vec<_>>().chunks(3) {
        let set_1: HashSet<char> = triple[0].chars().into_iter().collect();
        let set_2: HashSet<char> = triple[1].chars().into_iter().collect();
        let set_3: HashSet<char> = triple[2].chars().into_iter().collect();
        for s in set_1 {
            if set_2.contains(&s) && set_3.contains(&s) {
                if s as u32 >= 97 {
                    score += s as u32 - 96
                } else {
                    score += s as u32 - 38
                }
            }
        }
    }

    return Some(score);
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 3);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 3);
        assert_eq!(part_one(&input), None);
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 3);
        assert_eq!(part_two(&input), None);
    }
}
