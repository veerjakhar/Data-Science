import numpy as np

array1 = np.ones((4, 5))

array2 = np.zeros((3, 3))

array3 = np.arange(25).reshape(5, 5)

array4 = np.arange(24)

print(array1)
print("Shape: ", array1.shape)
print("Dimensions: ", array1.ndim)
print("Size: ", array1.size)
print("Memory Used: ", array1.nbytes, "bytes")

print("Shape: ", array2.shape)
print("Dimensions: ", array2.ndim)
print("Size: ", array2.size)
print("Memory Used: ", array2.nbytes, "bytes")

print(array3)
print("Shape: ", array3.shape)
print("Dimensions: ", array3.ndim)
print("Size: ", array3.size)
print("Memory Used: ", array3.nbytes, "bytes")

print(array4)
 
shapes = [
    (1, 24),
    (2, 12),
    (3, 8),
    (4, 6),
    (6, 4),
    (8, 3),
    (12, 2),
    (24, 1)
]

for shape in shapes:
    print("\n Shape: ", shape)
    print(array4.reshape(shape) )