from enum import Enum

class Instruction(Enum):
    NOOP = 0
    ADDX = 1

def parse(lines):
    for line in lines:
        l = line.rstrip()
        if l[0] == "a":
            yield (Instruction.ADDX, int(l.split()[1]))
        else:
            yield (Instruction.NOOP, 0)

data = open("input10.txt").readlines()
code = [p for p in parse(data)]

X_after_cycle = [1] #start at cycle 0
for ins,val in code:
    if ins == Instruction.NOOP:
        X_after_cycle.append(X_after_cycle[-1])
    else:
        X_after_cycle.append(X_after_cycle[-1])
        X_after_cycle.append(X_after_cycle[-1] + val)
print(X_after_cycle[19]*20+X_after_cycle[59]*60+X_after_cycle[99]*100+X_after_cycle[139]*140+X_after_cycle[179]*180+X_after_cycle[219]*220) 

crt=""
for cycle,X in enumerate(X_after_cycle[:-1]): #nothing happens after final cycle
    pixel = cycle % 40
    if pixel in [X-1,X,X+1]:
        crt += "#"
    else:
        crt += "."
    if pixel == 39 and cycle != len(X_after_cycle)-2: #no need for trailing \n
        crt += "\n"
print(crt)#is it cheating not implementing an ascii art to char function? =P
