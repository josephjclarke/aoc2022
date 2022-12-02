from enum import Enum


class Play(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0


def parse(c):
    if c == "A" or c == "X":
        return Play.ROCK
    elif c == "B" or c == "Y":
        return Play.PAPER
    elif c == "C" or c == "Z":
        return Play.SCISSORS
    else:
        raise SystemExit("Invalid Input")


def convert(me):
    if me == Play.ROCK:
        return Result.LOSE
    elif me == Play.PAPER:
        return Result.DRAW
    else:
        return Result.WIN


def outcome(op, me):
    if op == me:
        return Result.DRAW
    if (op == Play.ROCK and me == Play.PAPER) or (
            op == Play.PAPER and me == Play.SCISSORS) or (op == Play.SCISSORS
                                                          and me == Play.ROCK):
        return Result.WIN
    else:
        return Result.LOSE


def score(outcome, me):
    return outcome.value + me.value


def required_play(goal, op):
    if goal == Result.WIN:
        if op == Play.ROCK: return Play.PAPER
        elif op == Play.SCISSORS: return Play.ROCK
        else: return Play.SCISSORS
    elif goal == Result.LOSE:
        if op == Play.ROCK: return Play.SCISSORS
        elif op == Play.PAPER: return Play.ROCK
        else: return Play.PAPER
    else:
        return op


oponent_strat = []
my_strat = []

with open("input02.txt") as f:
    for line in f:
        o, m = map(parse, line.split())
        oponent_strat.append(o)
        my_strat.append(m)

print(sum(map(score, (map(outcome, oponent_strat, my_strat)), my_strat)))

target = map(convert, my_strat)
my_play = list(map(required_play, target, oponent_strat))
ocs = list(map(outcome, oponent_strat, my_play))
print(sum(map(score, map(outcome, oponent_strat, my_play), my_play)))
