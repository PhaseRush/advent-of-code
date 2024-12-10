type Coord = {
    y: number,
    x: number,
}

const parse_input = (text: string): number[][] => {
    return text.split("\r\n")
        .map(row => row.split("")
            .map(i => Number(i)))
}

const find_heads = (grid: Number[][]): Coord[] => {
    const heads: Coord[] = []
    for (const [y, row] of grid.entries()) {
        for (const [x, val] of row.entries()) {
            if (val == 0) {
                heads.push({y, x})
            }
        }
    }
    return heads;
}

const traverse_head = (head: Coord, grid: number[][]) => {
    const dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]];

    const seen_paths: Set<Coord[]> = new Set();
    const q: Coord[][] = [[head]]
    while (q.length > 0) {
        const curr_path = q.shift()! // I know this is N
        const {y, x} = curr_path.at(-1)!
        const curr_val = grid[y][x];
        if (curr_val == 9) {
            seen_paths.add(curr_path)
            continue;
        }

        for (const [dy, dx] of dirs) {
            const next_y = y + dy, next_x = x + dx;
            if (0 <= next_y && next_y < grid.length &&
                0 <= next_x && next_x < grid[0].length) {
                const next_val = grid[next_y][next_x];
                if (next_val == curr_val + 1) {
                    const next_path = curr_path.slice();
                    next_path.push({y: next_y, x: next_x});
                    q.push(next_path)
                }
            }
        }
    }
    return seen_paths.size;
}


const grid = parse_input(await Bun.file("./2024/10/input.txt").text());
const heads = find_heads(grid);
const score = heads.reduce((acc, head) => acc + traverse_head(head, grid), 0)
console.log(score);


