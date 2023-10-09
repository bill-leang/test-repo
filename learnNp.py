import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6, 7, 8])
arr3 = np.array([arr1, arr2])
arr4 = np.array([arr3, arr3])
print(arr4)
for i, val in enumerate(np.nditer(arr4)):
    print(f'{i+1}. {val}')
