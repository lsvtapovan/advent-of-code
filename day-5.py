import numpy as np
import pandas as pd

def format(input: str):
    return np.array([int(y) for y in np.ravel([x.split(',') for x in input.split(' -> ')])])

dat = pd.read_table('day-5.txt', header=None)
dat = np.array([format(x) for x in dat[0].values])

# Filter this list to include only horizontal and vertical lines.
hv_dat = np.array([x for x in dat if ((x[0] == x[2]) or (x[1] == x[3]))])
x_max = np.max(hv_dat[:, [0, 2]])
y_max = np.max(hv_dat[:, [1, 3]])

grid = np.zeros([x_max + 1, y_max + 1])
for row in hv_dat:
    if row[0] == row[2]:
        grid[row[0], np.min([row[1], row[3]]): np.max([row[1], row[3]]) + 1] += 1

    elif row[1] == row[3]:
        grid[np.min([row[0], row[2]]): np.max([row[0], row[2]]) + 1, row[1]] += 1

print(np.sum(grid >= 2))

# Diagonals included.
x_max = np.max(dat[:, [0, 2]])
y_max = np.max(dat[:, [1, 3]])

grid = np.zeros([x_max + 1, y_max + 1])
for row in dat:
    if row[0] == row[2]:
        grid[row[0], np.min([row[1], row[3]]): np.max([row[1], row[3]]) + 1] += 1

    elif row[1] == row[3]:
        grid[np.min([row[0], row[2]]): np.max([row[0], row[2]]) + 1, row[1]] += 1

    # Diagonals.
    else: 
        assert(abs(row[0] - row[2]) == abs(row[1] - row[3]))
        x_start, x_end, y_start, y_end = row[0], row[2], row[1], row[3]
        x_increasing = 1 if x_end > x_start else -1
        y_increasing = 1 if y_end > y_start else -1
        length = abs(x_end - x_start) + 1

        for ix in range(length):
            grid[x_start + ix*x_increasing, y_start + ix*y_increasing] += 1
        
print(np.sum(grid >= 2))

pass