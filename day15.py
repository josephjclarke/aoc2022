critical_y = 2_000_000
bound      = 4_000_000

def l1(a, b):
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))

def cmplx(a):
    return a[0]+1j*a[1]

sensors, beacons = zip(
    *[(cmplx(list(map(lambda x: int(x.split("=")[1]), l[10:].split(",")))),
       cmplx(list(map(lambda x: int(x.split("=")[1]), r[22:].split(",")))))
      for l, r in
      [line.rstrip().split(":") for line in open("input15.txt").readlines()]])


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

def test(z):
    if int(z.real) not in range(0,bound) or int(z.imag) not in range(0,bound):
        return False
    for s,b in zip(sensors,beacons):
        if l1(z,s) <= l1(s,b):
            return False
    return True

def onlypoint():
    for s,b in zip(sensors,beacons):
        d = l1(s,b)
        #must fall just outside the boundary of a scanned zone
        circle = [s + x + 1j*(d+1 - x) for x in range(-d-1,d+2)] + [s + x -1j*(d+1-x) for x in range(-d-1,d+2)]
        for p in circle:
            if test(p):
                return p

p = onlypoint()
print(int(p.real * 4000000 + p.imag)) 
