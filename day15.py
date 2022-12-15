def l1(a,b):
    return int(abs(a.real-b.real) + abs(b.imag - b.imag))

sensors,beacons = zip(*[(list(map(lambda x: int(x.split("=")[1]), l[10:].split(","))),
           list(map(lambda x: int(x.split("=")[1]), r[22:].split(","))))
          for l, r in [line.rstrip().split(":") for line in open("input15.test").readlines()]])

critical_y = 10#2000000
sensors = [s[0] + 1j *s[1] for s in sensors]
beacons = [b[0] + 1j *b[1] for b in beacons]


nobeacons = set()
for s,b in zip(sensors,beacons):
    maxdist = l1(s,b)
    nobeacons.update([x for x in range(int(s.real)-maxdist,int(s.real)+maxdist) if l1(s,x + critical_y *1j) <= maxdist])
#remove beacons
print(len(nobeacons - {b.real for b in beacons if b.imag==critical_y}))
