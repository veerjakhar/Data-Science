import numpy as np

array = np.array([5, 6, 7, 8, 1, 2, 3, 4])

array1 = np.arange(9).reshape((3, 3))
array2 = np.arange(49).reshape((7, 7))

print(array[0:4])
print(array[:7])

print(array[5:])
print(array[::2])

print(array[::-2])

print(array1)

print(array1[0:1, 0:1])

print(array2[2:5, 2:5])