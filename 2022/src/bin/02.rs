use std::collections::HashMap;

pub fn part_one(input: &str) -> Option<u32> {
    let mut score = 0;
    let outcomes = HashMap::from([
        ("A X", 4),
        ("A Y", 8),
        ("A Z", 3),
        ("B X", 1),
        ("B Y", 5),
        ("B Z", 9),
        ("C X", 7),
        ("C Y", 2),
        ("C Z", 6)
    ]);

    for matchup in input.split("\n") {
        score += outcomes.get(matchup).unwrap();
    }
    return Some(score);
}

pub fn part_two(input: &str) -> Option<u32> {
    let mut score = 0;

    let pairings = HashMap::from([
        ("X", HashMap::from([("A", 3), ("B", 1), ("C", 2)])),
        ("Y", HashMap::from([("A", 4), ("B", 5), ("C", 6)])),
        ("Z", HashMap::from([("A", 8), ("B", 9), ("C", 7)])),
    ]);

    for matchup in input.split("\n") {
        score += pairings
            .get(&matchup[2..3]).unwrap()
            .get(&matchup[0..1]).unwrap();
    }
    return Some(score);
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 2);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 2);
        assert_eq!(part_one(&input), None);
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 2);
        assert_eq!(part_two(&input), None);
    }
}
