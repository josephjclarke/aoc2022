import numpy as np


def l1(a, b):
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))


def nearestSensor(point, sensors):
    m = float("inf")
    for idx in range(len(sensors)):
        n = l1(point, sensors[idx])
        if n < m:
            ret = idx
            m = n
    return ret


sensors, beacons = zip(
    *[(list(map(lambda x: int(x.split("=")[1]), l[10:].split(","))),
       list(map(lambda x: int(x.split("=")[1]), r[22:].split(","))))
      for l, r in
      [line.rstrip().split(":") for line in open("input15.txt").readlines()]])

critical_y = 2000000
bound = 4000000

sensors = [s[0] + 1j * s[1] for s in sensors]
beacons = [b[0] + 1j * b[1] for b in beacons]

nobeacons = set()
for s, b in zip(sensors, beacons):
    maxdist = l1(s, b)
    nobeacons.update([
        x for x in range(int(s.real) - maxdist,
                         int(s.real) + maxdist)
        if l1(s, x + critical_y * 1j) <= maxdist
    ])

nobeacons -= {int(b.real) for b in beacons if int(b.imag) == critical_y}
print(len(nobeacons))

idx = list(range(len(sensors)))
ds = [-l1(b, s) for s, b in zip(sensors, beacons)]
idx.sort(key=ds.__getitem__)
sensors = list(map(sensors.__getitem__, idx))
beacons = list(map(beacons.__getitem__, idx))
for x in range(0, bound):
    for y in range(0, bound):
        p = x + 1j * y
        not_excluded = True
        for s, b in zip(sensors, beacons):
            if l1(s, p) <= l1(s, b):
                not_excluded = False
                break
        if not_excluded:
            print(int(bound * p.real + p.imag))
            raise SystemExit
