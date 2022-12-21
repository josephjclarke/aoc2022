import functools

data = open("input16.txt").readlines()
    
graph = {}
for line in data:
    words = line.rstrip().split()
    graph[words[1]] = (int(words[4].split("=")[1][:-1]),list(map(lambda x: x.replace(","," ").rstrip(),words[9:])))


@functools.cache
def distances(start):
    d = {n:float("inf") for n in graph.keys()}
    d[start] = 0.0
    unvisited = list(graph.keys())
    cn = start
    queue = sorted(unvisited,key=lambda x: d[x])
    while len(queue) > 0:
        cn = queue.pop(0)
        for child in graph[cn][1]:
            if child in unvisited:
                d[child] = min(d[cn] + 1,d[child])
        unvisited.remove(cn)
        queue = sorted(unvisited,key=lambda x: d[x])
    return d

@functools.cache
def bestmove(start,timeleft,openvalves):
    d = distances(start)
    possible_nodes = [g for g in graph if d[g] + 2 <= timeleft and g not in openvalves and graph[g][0] > 0]
    preleased = [graph[g][0] * (timeleft - d[g] - 1) for g in possible_nodes]
    totrel = 0
    nextrel = [bestmove(g,timeleft-d[g]-1,openvalves + (g,)) for g in possible_nodes]
    for i in range(len(nextrel)):
        totrel=max(totrel,nextrel[i]+preleased[i])
    return totrel


@functools.cache
def bestmoveele(s1,s2,t1,t2,openvalves):
    if t1 <= t2:
        me = s1
        tlme=t1
        ele=s2
        tlele=t2
    else:
        me = s2
        tlme=t2
        ele=s1
        tlele=t1

    dme = distances(me)
    dele = distances(ele)
    pnme = [g for g in graph if dme[g]+2 <= tlme and g not in openvalves and graph[g][0] > 0]
    pnele= [g for g in graph if dele[g]+2 <= tlele and g not in openvalves and graph[g][0]>0]
    if len(pnme) == 0:
        return bestmove(ele,tlele,openvalves)
    if len(pnele) == 0:
        return bestmove(me,tlme,openvalves)
    prme = [graph[g][0] * (tlme - dme[g] - 1) for g in pnme]
    prele= [graph[g][0] * (tlele-dele[g] - 1) for g in pnele]
    totrel=0
    for i in range(len(prme)):
        for j in range(len(prele)):
            if pnme[i] == pnele[j]: 
                continue
            totrel = max(totrel,prme[i] + prele[j] + bestmoveele(pnme[i],pnele[j],tlme-dme[pnme[i]]-1,tlele-dele[pnele[j]]-1,openvalves+(pnme[i],pnele[j])))
    return totrel

print(int(bestmove("AA",30,())))
print(int(bestmoveele("AA","AA",26,26,())))
