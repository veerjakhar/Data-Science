import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
numbers1 = np.array([5, 3, 8 ,1 ,0, 7, 3, 5, 1])
numbers10 = np.array(range(1, 10))
temp = np.array([71, 61, 80, 79, 68, 69, 90])
print(numbers+numbers1)
print("Highest: ", np.max(temp))
print("Minimun: ", np.min(temp))
print("Average: ", np.mean(temp))
print(numbers10)