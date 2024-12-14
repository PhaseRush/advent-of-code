use std::collections::BTreeMap;

pub struct TreeNode {
    pub key: Box<String>,
    pub val: usize,
    pub parent: Option<Box<TreeNode>>,
    pub left: Vec<TreeNode>,
    pub right: Vec<TreeNode>,
}

impl TreeNode {
    pub fn new(
        key: Box<String>,
        val: usize,
        parent: Option<Box<TreeNode>>,
        left: Vec<TreeNode>,
        right: Vec<TreeNode>,
    ) -> Self {
        TreeNode {
            key,
            val,
            parent,
            left,
            right,
        }
    }
}

pub struct Tree {
    root: Option<TreeNode>,
}

impl Tree {
    pub fn new(root: TreeNode) -> Self {
        Tree {
            root: None,
        }
    }
    // pub fn iter(&self) -> PreOrderIter {
    //     PreOrderIter::new(self.root.as_ref())
    // }
}

pub fn part_one(input: &str) -> Option<u32> {
    // let mut tree = BTreeMap::from([("/", 0)]);
    let mut count = 0;
    let mut tree = Tree::new(
        TreeNode::new(Box::new("/".parse().unwrap()),
                      -1,
                      None,
                      vec![],
                      vec![]));
    let mut curr_node;

    for line in input[1..input.len()].split_whitespace() {
        let parsed_line = line.split_whitespace().collect::<Vec<&str>>();
        let action = parsed_line[0];
        match action {
            "$" => {
                println!("{:?}", parsed_line);
                match parsed_line[1] {
                    "cd" => {}
                    "ls" => {}
                    _ => {}
                }
            }
            "dir" => {
                println!("other");
            }
            _ => {}
        }
    }

    return Some(count);
}

pub fn part_two(input: &str) -> Option<u32> {
    None
}

fn main() {
    let input = &advent_of_code::read_file("inputs", 7);
    advent_of_code::solve!(1, part_one, input);
    advent_of_code::solve!(2, part_two, input);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let input = advent_of_code::read_file("examples", 7);
        assert_eq!(part_one(&input), None);
    }

    #[test]
    fn test_part_two() {
        let input = advent_of_code::read_file("examples", 7);
        assert_eq!(part_two(&input), None);
    }
}
