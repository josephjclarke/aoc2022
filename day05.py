from enum import Enum


class Instruction(Enum):
    MOVE = 1


class Statement:

    def __init__(self, ins, qty, src, dest):
        self.ins = ins
        self.qty = qty
        self.src = src
        self.dest = dest

    def __str__(self):
        return f"{self.ins} {self.qty} {self.src} {self.dest}"

    def __repr__(self):
        return str(self)


def run9000(tape, stacks):
    for statement in tape:
        if statement.ins == Instruction.MOVE:
            for i in range(statement.qty):
                stacks[statement.dest - 1].append(
                    stacks[statement.src - 1].pop())
        else:
            raise SystemExit(f"Invalid Instruction {statement.ins}")
    return stacks

def run9001(tape, stacks):
    for statement in tape:
        if statement.ins == Instruction.MOVE:
            crates = stacks[statement.src-1][-statement.qty:]
            stacks[statement.src-1] = stacks[statement.src-1][:-statement.qty]
            for c in crates:
                stacks[statement.dest-1].append(c)
        else:
            raise SystemExit(f"Invalid Instruction {statement.ins}")
    return stacks

def makeTape(lines):
    tape = []
    for line in lines:
        words = line.rstrip().split()
        if words[0] == "move":
            tape.append(
                Statement(Instruction.MOVE, 
                          int(words[1]),
                          int(words[3]),
                          int(words[5])))
    return tape


def makeStacks(lines):
    ip = [[line[i:i+4] for i in range(0,len(line),4)] for line in lines]
    number_of_stacks = len(ip[0])
    stacks = [[""] for i in range(number_of_stacks)]
    for s in ip[1:]:
        for i in range(number_of_stacks):
            value = s[i][1]
            if value == " ":
                continue
            stacks[i].append(value)
    return stacks

data = open("input05.txt").readlines()

for i in range(len(data)):
    if data[i] == "\n":
        changeLine = i
        break

tape = makeTape(data[changeLine + 1:])
stacks = makeStacks(data[:changeLine][::-1])
final_stacks = run9000(tape,stacks)
print("".join([fs[-1] for fs in final_stacks]))
stacks = makeStacks(data[:changeLine][::-1])
final_stacks = run9001(tape,stacks)
print("".join([fs[-1] for fs in final_stacks]))