import itertools
import timeit

import tqdm


class Computer:

    def __init__(self, A, B, C, program):
        self.A = A
        self.B = B
        self.C = C
        self.pointer = 0
        self.program = program

    def registers(self):
        print(self.A, self.B, self.C, sep="\n")

    def combo_operand(self, i):
        match i:
            case 0 | 1 | 2 | 3:
                return i
            case 4:
                return self.A
            case 5:
                return self.B
            case 6:
                return self.C

    def process(self, out):
        while self.pointer in range(len(self.program)):
            match self.program[self.pointer: self.pointer + 2]:
                case 0, operand:
                    self.A = self.A // (2 ** self.combo_operand(operand))
                case 1, operand:
                    self.B = self.B ^ operand
                case 2, operand:
                    self.B = self.combo_operand(operand) % 8
                case 3, operand:
                    if self.A:
                        self.pointer = operand
                    else:
                        self.pointer -= 2  # reset
                case 4, operand:
                    self.B = self.B ^ self.C
                case 5, operand:
                    # val = self.combo_operand(operand) % 8
                    out.append(self.combo_operand(operand) % 8)
                case 6, operand:
                    self.B = self.A // (2 ** self.combo_operand(operand))
                case 7, operand:
                    self.C = self.A // (2 ** self.combo_operand(operand))

            self.pointer += 2
        return out


with open('input.txt') as f:
    lines = f.read().splitlines()

    instructions = list(map(int, lines[4].split()[1].split(",")))
    print("start", instructions)


def sim(c, a):
    out = []
    pointer = 0
    while pointer in range(len(instructions)):
        pointer, val = c.process(instructions[pointer], instructions[pointer + 1], out)
        if len(out) == len(instructions):
            if out == instructions:
                print("Found")
                return a
            else:
                return None


def find(a, i):
    c = Computer(a, 0, 0, instructions)
    out = []
    c.process(out)
    if out == instructions:
        print(a)
    if out == instructions[-i:] or i == 0:
        for n in range(8):
            find(8 * a + n, i + 1)


def f():
    find(0, 0)
    # pass


if __name__ == '__main__':
    iters = 1
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.2f} s")
