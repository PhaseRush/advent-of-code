fn get_stacks() -> Vec<Vec<&'static str>> {
    return vec![
        vec!["Z", "J", "G"],
        vec!["Q", "L", "R", "P", "W", "F", "V", "C"],
        vec!["F", "P", "M", "C", "L", "G", "R"],
        vec!["L", "F", "B", "W", "P", "H", "M"],
        vec!["G", "C", "F", "S", "V", "Q"],
        vec!["W", "H", "J", "Z", "M", "Q", "T", "L"],
        vec!["H", "F", "S", "B", "V"],
        vec!["F", "J", "Z", "S"],
        vec!["M", "C", "D", "P", "F", "H", "B", "T"],
    ];
}

fn get_small_stacks() -> Vec<Vec<&'static str>> {
    return vec![
        vec!["Z", "N"],
        vec!["M", "C", "D"],
        vec!["P"],
    ];
}

pub fn get_tops(stacks: Vec<Vec<&str>>) -> String {
    let mut tops = String::new();
    for i in 0..stacks.len() {
        tops.push(stacks[i].last().unwrap().chars().nth(0).unwrap())
    }
    println!("{}", tops);
    return tops;
}

pub fn part_one(input: &str) -> Option<String> {
    let mut stacks = get_stacks();
    for line in input.split("\n") {
        let words = line.split_whitespace()
            .map(str::to_string)
            .collect::<Vec<String>>();

        let quantity = words[1].parse::<usize>().unwrap();
        let origin = words[3].parse::<usize>().unwrap() - 1;
        let dest = words[5].parse::<usize>().unwrap() - 1;

        for _i in 0..quantity {
            let item = stacks[origin].pop().unwrap();
            stacks[dest].push(item);
            println!()
        }
    }

    return Some(get_tops(stacks));
}


pub fn part_two(input: &str) -> Option<String> {
    let mut stacks: Vec<Vec<&str>> = get_stacks();
    for line in input.split("\n") {
        let words = line.split_whitespace()
            .map(str::to_string)
            .collect::<Vec<String>>();

        let quantity = words[1].parse::<usize>().unwrap();
        let origin = words[3].parse::<usize>().unwrap() - 1;
        let dest = words[5].parse::<usize>().unwrap() - 1;

        let mut to_move = Vec::new();
        for _i in 0..quantity {
            to_move.push(stacks[origin].pop().unwrap());
        }
        to_move.reverse();
        stacks[dest].extend(to_move);
    }

    return Some(get_tops(stacks));
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 5);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 5);
        assert_eq!(part_one(&input), None);
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 5);
        assert_eq!(part_two(&input), None);
    }
}
