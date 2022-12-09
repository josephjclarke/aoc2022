import enum


class Move(enum.Enum):
    R = 0
    U = 1
    L = 2
    D = 3


def mtoMove(m):
    if m == "R":
        return Move.R
    elif m == "U":
        return Move.U
    elif m == "L":
        return Move.L
    elif m == "D":
        return Move.D
    else:
        raise SystemExit("Invalid Direction")


def parse(lines):
    for line in lines:
        m, n = line.rstrip().split()
        move = mtoMove(m)
        yield from [move for i in range(int(n))]


def updatePosition(initial, move):
    (x, y) = initial
    if move == Move.U:
        return (x, y + 1)
    elif move == Move.D:
        return (x, y - 1)
    elif move == Move.R:
        return (x + 1, y)
    elif move == Move.L:
        return (x - 1, y)
    else:
        raise SystemExit("Invalid Move")


def sign(x):
    if x == 0:
        return 0
    else:
        return 1 if x > 0 else -1


def moveTail(heads, tails):
    for i in range(len(heads) - 1):
        H = heads[i + 1]
        T = tails[i]
        dx = H[0] - T[0]
        dy = H[1] - T[1]
        if abs(dx) > 1 or abs(dy) > 1:
            tails.append((T[0] + sign(dx), T[1] + sign(dy)))
        else:
            tails.append(T)
    return tails


data = open("input09.txt").readlines()
moves = [move for move in parse(data)]
poss = [[(0, 0)] for i in range(10)]

for move in moves:
    poss[0].append(updatePosition(poss[0][-1], move))

for i in range(1, len(poss)):
    poss[i] = moveTail(poss[i - 1], poss[i])

print(len(set(poss[1])))
print(len(set(poss[-1])))
