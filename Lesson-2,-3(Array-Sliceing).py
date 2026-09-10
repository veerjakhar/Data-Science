import numpy as np

array = np.array([5, 6, 7, 8, 1, 2, 3, 4])

array1 = np.arange(9).reshape((3, 3))
array2 = np.arange(49).reshape((7, 7))
array3 = np.array(range(1, 16))

'''print(array[0:5]) # --  First
print(array[:7]) # -- First

print(array[3:])  # -- Cut out the first numbers
print(array[::3]) # -- Every certain element

print(array[::-1]) # -- Backwords every certian element

print(array1)

print(array1[0:1, 0:1])

print(array2)

print(array2[2:5, 2:5]) # -- Taking out a certain area (3x3)
print(array2[0:1, 0:7]) # -- First row
print(array2[:, -1]) # -- Last collumn '''


print(array3)
a = array3[array3 < 8]
b = array3[array3 >= 10]
c = array3[array3 %2 == 1]
print(a)
print(b)
print(array3[::2])
print(c)

