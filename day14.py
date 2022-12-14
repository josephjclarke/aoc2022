from enum import Enum


class material(Enum):
    ROCK = 0
    SAND = 1


def pp(c):
    rocks = c.keys()
    ii = [r[1] for r in rocks]
    jj = [r[0] for r in rocks]
    for i in range(max(ii) + 1):
        for j in range(min(jj), max(jj) + 1):
            if i == 0 and j == 500:
                print("+", end="")
            elif (j, i) in c:
                if c[(j, i)] == material.ROCK:
                    print("#", end="")
                else:
                    print("o", end="")
            else:
                print(".", end="")
        print("")


def advance(c, pos, minh):
    while True:
        returning = True
        test_poss = [(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] + 1),
                     (pos[0] + 1, pos[1] + 1)]
        if pos[1] > minh:
            return c, True
        for t in test_poss:
            if t not in c:
                c[t] = material.SAND
                del c[pos]
                pos = t
                returning = False
                break
        if returning:
            #pp(c)
            return c, False


def advance2(c, pos, minh):
    while True:
        returning = True
        test_poss = [(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] + 1),
                     (pos[0] + 1, pos[1] + 1)]
        for t in test_poss:
            if t not in c and t[1] < minh + 2:
                c[t] = material.SAND
                del c[pos]
                pos = t
                returning = False
                break
        if returning:
            return c, False


cave = {}
data = open("input14.txt").readlines()
for line in data:
    line = line.rstrip()
    poss = [p.rstrip() for p in line.split("->")]
    for i in range(len(poss) - 1):
        p1 = list(map(int, poss[i].split(",")))
        p2 = list(map(int, poss[i + 1].split(",")))
        cave[(p1[0], p1[1])] = material.ROCK
        cave[(p2[0], p2[1])] = material.ROCK
        if p1[0] == p2[0]:
            low = min(p1[1], p2[1])
            up = max(p1[1], p2[1])
            for i in range(low, up):
                cave[(p1[0], i)] = material.ROCK
        else:
            low = min(p1[0], p2[0])
            up = max(p1[0], p2[0])
            for i in range(low, up):
                cave[(i, p1[1])] = material.ROCK
cave2 = cave.copy()

minh = max([r[1] for r in cave.keys()])
count = 0
while True:
    cave[(500, 0)] = material.SAND
    oldcave = cave.copy()
    cave, done = advance(cave, (500, 0), minh)
    if done:
        break
    count += 1
print(count)

count = 1
while True:
    cave2[(500, 0)] = material.SAND
    cave2, done = advance2(cave2, (500, 0), minh)
    if (500, 0) in cave2:
        break
    count += 1
print(count)
