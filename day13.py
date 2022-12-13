import functools


def checkpairs(left, right):
    return maybecheckpairs(left, right)[1]


def maybecheckpairs(left, right):
    for l, r in zip(left, right):
        if type(l) == type(r) == int:
            if l != r:
                return (True, l < r)
        if type(l) == type(r) == list:
            yes, val = maybecheckpairs(l, r)
            if yes:
                return (True, val)
        if type(l) == list and type(r) == int:
            return maybecheckpairs(l, [r])
        if type(l) == int and type(r) == list:
            return maybecheckpairs([l], r)
    if len(left) == len(right):
        return (False, False)
    return (True, len(left) < len(right))


data = [l.rstrip() for l in open("input13.txt").readlines()]
pairs = [(eval(data[i]), eval(data[i + 1]))
         for i in range(0,
                        len(data) - 1, 3)]

right_order = [checkpairs(*p) for p in pairs]
print(sum([i + 1 for i, r in enumerate(right_order) if r]))

packets = [
    eval(l.rstrip())
    for i, l in enumerate(open("input13.txt").readlines()) if (i + 1) % 3 != 0
] + [[[2]], [[6]]]

sorted_packets = sorted(
    packets,
    key=functools.cmp_to_key(lambda item1, item2: 1
                             if checkpairs(item1, item2) else -1),
    reverse=True)

print(
    functools.reduce(lambda x, y: x * y, [
        i + 1 for i, p in enumerate(sorted_packets) if p == [[2]] or p == [[6]]
    ], 1))
