class Monkey:
    def __init__(self, items, op, testdiv, throwTrue, throwFalse):
        self.items = items
        self.op = op
        self.testdiv = testdiv
        self.throwTrue = throwTrue
        self.throwFalse = throwFalse
        self.inspected = 0

    def operation(self, old):
        return eval(self.op)


def parseMonkey(data):
    ms = [data[x:x + 7] for x in range(0, len(data), 7)]
    for m in ms:
        items = list(map(int, m[1].rstrip().split(":")[1].strip().split(",")))
        op = m[2].split(":")[1].rstrip().split("=")[1]
        testdiv = int(m[3].rstrip().split()[-1])
        throwTrue = int(m[4].rstrip().split()[-1])
        throwFalse = int(m[5].rstrip().split()[-1])
        yield Monkey(items, op, testdiv, throwTrue, throwFalse)


data = open("input11.txt").readlines()
monkeys = [m for m in parseMonkey(data)]
max_rounds = 20
for round in range(max_rounds):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspected += 1
            wl = monkey.operation(item) // 3
            if wl % monkey.testdiv == 0:
                monkeys[monkey.throwTrue].items.append(wl)
                monkey.items = monkey.items[1:]
            else:
                monkeys[monkey.throwFalse].items.append(wl)
                monkey.items = monkey.items[1:]

sm = sorted([m.inspected for m in monkeys])
print(sm[-2] * sm[-1])

monkeys = [m for m in parseMonkey(data)]
#Need to preserve mod structure i.e if wl % testdiv = 0 or not.
#If testdiv | wl, then testdiv | (wl % N) where N is a multiple of testdiv
#Hence if N is a multoiple of all the testdivs it suffices to work
#modulo N which keeps the numbers small enough
N = 1
for m in monkeys:
    N *= m.testdiv
max_rounds = 10000
for round in range(max_rounds):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspected += 1
            wl = monkey.operation(item) % N
            if wl % monkey.testdiv == 0:
                monkeys[monkey.throwTrue].items.append(wl)
                monkey.items = monkey.items[1:]
            else:
                monkeys[monkey.throwFalse].items.append(wl)
                monkey.items = monkey.items[1:]

sm = sorted([m.inspected for m in monkeys])
print(sm[-2] * sm[-1])
