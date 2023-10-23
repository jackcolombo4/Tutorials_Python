import numpy as np
import scipy.ndimage as nd

Existing_example_arrayV0 = np.array([[0, 0, 1, 0, 0, 0, 0], 
                                     [0, 1, 1, 1, 0, 0, 0], 
                                     [0, 1, 1, 1, 1, 0, 0], 
                                     [1, 1, 1, 1, 1, 0, 0], 
                                     [0, 1, 1, 1, 1, 0, 0], 
                                     [0, 1, 1, 0, 0, 0, 0]])

# First iteration
mask = nd.binary_erosion(Existing_example_arrayV0 >= 1, structure=[[1, 1, 1]])
Existing_example_arrayV1 = Existing_example_arrayV0.copy()
Existing_example_arrayV1[mask] += 100

# Subsequent iterations
for i in range(1, 3):
    mask = nd.binary_erosion(Existing_example_arrayV1 >= 1, structure=[[1, 1, 1]])
    Existing_example_arrayV1[mask] += 100
    print(f'Existing_example_arrayV{i+1} = {Existing_example_arrayV1}')