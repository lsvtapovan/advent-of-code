import pandas as pd
import numpy as np

data = pd.read_table('day-2-input.txt', delimiter=' ', header=None)
start = np.array([0, 0]) # horizontal, depth
start_2 = np.array([0, 0, 0]) # horizontal, depth, aim

def update_coord(current_coords: np.array, instruction: np.array):
    if instruction[0] == 'forward':
        current_coords[0] += instruction[1]
    elif instruction[0] == 'down':
        current_coords[1] += instruction[1]
    elif instruction[0] == 'up':
        current_coords[1] -= instruction[1]
    
    return current_coords

def update_coord_2(current_coords: np.array, instruction: np.array):
    if instruction[0] == 'forward':
        current_coords[0] += instruction[1]
        current_coords[1] += instruction[1] * current_coords[2]
    elif instruction[0] == 'down':
        current_coords[2] += instruction[1]
    elif instruction[0] == 'up':
        current_coords[2] -= instruction[1]
    
    return current_coords

for instruction in data.values:
    update_coord(start, instruction)
    update_coord_2(start_2, instruction)

output = np.prod(start)
output_2 = np.prod(start_2[:2])
