lines = [line.rstrip().split(":") for line in open("input15.txt").readlines()]
lines2 = [(list(map(lambda x: int(x.split("=")[1]), l[10:].split(","))),
           list(map(lambda x: int(x.split("=")[1]), r[22:].split(","))))
          for l, r in lines]
sensors, beacons = zip(*lines2)
print(sensors, beacons)
