import numpy as np
data = np.array(list(map(list,[line.rstrip() for line in open("input12.txt").readlines()])))
sidx = np.nonzero(data == "S")
eidx = np.nonzero(data == "E")
data[sidx] = "a"
data[eidx] = "z"

heights = data.view(np.int32) - 97
adj = np.zeros((heights.size,heights.size),dtype="bool")
fh = heights.flatten()

distances = np.full_like(fh,np.inf,dtype="float")

for idx in np.ndindex(heights.shape):
    for i in range(max(0,idx[0]-1),min(idx[0]+2,heights.shape[0])):
        for j in range(max(0,idx[1]-1),min(idx[1]+2,heights.shape[1])):
            if not np.logical_xor(i==idx[0] ,j==idx[1]): continue
            if heights[i,j] >= heights[idx] -1:
                i1 = np.ravel_multi_index(idx,heights.shape)
                j1 = np.ravel_multi_index((i,j),heights.shape)
                adj[i1,j1] = True



end = np.ravel_multi_index(eidx,heights.shape)
distances[end] = 0
explored = np.zeros_like(heights,dtype="bool")
explored[eidx] = True
q = [end.item()]

for idx in q:
    td = distances[idx] + 1
    for nodes in np.nonzero(adj[idx])[0]:
        if not explored[np.unravel_index(nodes,heights.shape)]:
            explored[np.unravel_index(nodes,heights.shape)] = True
            if td < distances[nodes]:
                distances[nodes] = td
            q.append(nodes)

print(int(distances.reshape(heights.shape)[sidx].item()))
print(int(distances.reshape(heights.shape)[np.nonzero(heights==0)].min()))
