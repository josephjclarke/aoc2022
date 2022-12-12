data = open("input12.txt").readlines()

heights = []
for i in range(len(data)):
    heights.append([])
    for k in range(len(data[0]) - 1):
        if data[i][k] == "S":
            start_idx = (i, k)
            heights[i].append(ord("a") - 97)
        elif data[i][k] == "E":
            end_idx = (i, k)
            heights[i].append(ord("z") - 97)
        else:
            heights[i].append(ord(data[i][k]) - 97)


def connected(a, b):
    ha = heights[a[0]][a[1]]
    hb = heights[b[0]][b[1]]
    return hb <= ha + 1


graph = {}

for i in range(len(heights)):
    for j in range(len(heights[0])):
        graph[(i, j)] = []
        adj = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for a in adj:
            if a[0] < 0 or a[0] > len(heights) - 1 or a[1] < 0 or a[1] > len(
                    heights[0]) - 1:
                continue
            if connected((i, j), a):
                graph[(i, j)].append(a)


def subgraph_idx(idx):
    sg = []
    nodes2check = [idx]
    for cidx in nodes2check:
        if cidx in sg:
            continue
        sg.append(cidx)
        for n in graph[cidx]:
            nodes2check.append(n)
    return sg


def getmindist(si):
    distances = [[float("inf") for i in range(len(heights[0]))]
                 for j in range(len(heights))]
    distances[si[0]][si[1]] = 0

    sg = subgraph_idx(si)
    unvisited = {s: True for s in sg}
    cidx = si
    while True:
        for node in graph[cidx]:
            td = distances[cidx[0]][cidx[1]] + 1
            if distances[node[0]][node[1]] > td:
                distances[node[0]][node[1]] = td
        unvisited[cidx] = False
        if cidx == end_idx:
            break
        mv = float("inf")
        for uv, val in unvisited.items():
            if not val:
                continue
            if mv > distances[uv[0]][uv[1]]:
                mv = distances[uv[0]][uv[1]]
                cidx = uv
        if unvisited[cidx] == False:
            break

    return distances[end_idx[0]][end_idx[1]]


print(getmindist(start_idx))
start_points = [(i, j) for i in range(len(heights))
                for j in range(len(heights[0])) if heights[i][j] == 0]
md = [getmindist(si) for si in start_points]
print(min(md))
