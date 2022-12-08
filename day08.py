import numpy as np

data = open("input08.test").readlines()

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

def ss(arr):
    count = np.zeros_like(arr)
    for i in range(arr.size):
        for j in range(i,0,-1):
            if arr[j-1] <= arr[i]:
                count[i] +=1
            else:
                break
    count[1:] = np.where(count[1:] == 0,1,count[1:])
    return count

for h in heights:
    print(ss(h),ss(h[::-1])[::-1])
score = np.ones_like(heights)
for i in range(heights.shape[0]):
    score[i] *= ss(heights[i])
    score[i][::-1] *= ss(heights[i][::-1])
for h in range(heights.shape[1]):
    score[:,i] *= ss(heights[:,i])
    score[:,i][::-1] *= ss(heights[:,i][::-1])
print(score)
