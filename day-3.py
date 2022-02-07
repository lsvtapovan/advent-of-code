from math import gamma
import numpy as np
import pandas as pd

dat = pd.read_table('day-3-input.txt', header=None, names=['bin'], dtype={'bin': str})
all_binaries = dat['bin'].values

maxs=[]
mins=[]
for ix in range(len(all_binaries[0])):
    bin_elements = [x[ix] for x in all_binaries]
    elems, counts = np.unique(bin_elements, return_counts=True)
    maxs.append(elems[0] if counts[0] > counts[1] else elems[1])
    mins.append(elems[0] if counts[0] < counts[1] else elems[1])

gamma_rate = int(''.join(maxs), 2)
epsilon_rate = int(''.join(mins), 2)
print(epsilon_rate * gamma_rate)

filtered_bin_array = np.array(all_binaries)
for ix in range(len(all_binaries[0])):
    bin_elements = np.array([x[ix] for x in filtered_bin_array])
    n_zero = sum(bin_elements == '0')
    n_ones = sum(bin_elements == '1')    
    maxs = '1' if n_ones >= n_zero else '0'
    filtered_bin_array = np.array([x for x in filtered_bin_array if x[ix] == maxs])

    if len(filtered_bin_array) == 1:
        break

oxygen_rate = int(''.join(filtered_bin_array[0]), 2)

filtered_bin_array = np.array(all_binaries)
for ix in range(len(all_binaries[0])):
    bin_elements = np.array([x[ix] for x in filtered_bin_array])
    n_zero = sum(bin_elements == '0')
    n_ones = sum(bin_elements == '1')    
    mins = '1' if n_ones < n_zero else '0'
    filtered_bin_array = np.array([x for x in filtered_bin_array if x[ix] == mins])

    if len(filtered_bin_array) == 1:
        break

co2_rate = int(''.join(filtered_bin_array[0]), 2)

print(oxygen_rate * co2_rate)
pass
