import numpy as np

data = open("input08.txt").readlines()

heights = np.zeros((len(data), len(data[0].rstrip())), dtype="int")
for i in range(heights.shape[0]):
    heights[i] = [int(c) for c in data[i].rstrip()]

left_maxs = np.maximum.accumulate(heights, axis=1)
right_maxs = np.maximum.accumulate(heights[:, ::-1], axis=1)
top_maxs = np.maximum.accumulate(heights, axis=0)
bottom_maxs = np.maximum.accumulate(heights[::-1, :], axis=0)

#Tree's are only visible when the running maximum changes
#we need to prepend a 0 to ensure the diff arrays line up with the
#heights array

visible_horizontally = np.logical_or(
    np.diff(left_maxs, axis=1, prepend=0),
    np.diff(right_maxs, axis=1, prepend=0)[:, ::-1])
visible_vertically = np.logical_or(
    np.diff(top_maxs, axis=0, prepend=0),
    np.diff(bottom_maxs, axis=0, prepend=0)[::-1, :])

visible = np.logical_or(visible_horizontally, visible_vertically)

#Set the edges to be visible
visible[0] = True
visible[-1] = True
visible[:, 0] = True
visible[:, -1] = True

print(visible.sum())


#feels like a hack
def ss(arr):
    count = np.zeros_like(arr)
    for i in range(count.size):
        A = (arr[:i] < arr[i])[::-1]
        for a in A:
            count[i] += 1
            if a == False:
                break
    return count

score = np.ones_like(heights)
for i in range(heights.shape[0]):
    score[i,:] *= ss(heights[i,:])
    score[i,:] *= ss(heights[i,:][::-1])[::-1]
for j in range(heights.shape[1]):
    score[:,j] *= ss(heights[:,j])
    score[:,j] *= ss(heights[:,j][::-1])[::-1]
print(score.max())
