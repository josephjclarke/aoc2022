def parseAssignment(s):
    start, stop = s.split("-")
    return int(start), int(stop)


def parseLine(line):
    left, right = line.split(",")
    return unwrapParse(left, right)


def unwrapParse(left, right):
    l1, l2 = parseAssignment(left)
    r1, r2 = parseAssignment(right)
    return l1, l2, r1, r2


def isContainedIn(line):
    l1, l2, r1, r2 = parseLine(line)

    if l1 <= r1 and l2 >= r2:
        return True
    if r1 <= l1 and r2 >= l2:
        return True
    else:
        return False


def ov(l1, l2, r1, r2):
    if r1 < l1:
        return ov(r1, r2, l1, l2)
    if l2 >= r1:
        return True
    else:
        return False


def overlaps(line):
    return ov(*parseLine(line))


data = open("input04.txt").readlines()
print(sum([isContainedIn(line.rstrip()) for line in data]))
print(sum([overlaps(line.rstrip()) for line in data]))
