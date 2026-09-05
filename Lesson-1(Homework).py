import numpy as np

array1 = np.array(range(1, 17)).reshape(4, 4)

count0 = 0
count1 = 0

for i in range(4):
    for j in range(4):
        print(array1[i][j])
        if array1[i][j] %2 == 0:
            count0 = count0 + 1
            array1[i][j] = 0
        elif array1[i][j] %2 == 1:
            count1 = count1 + 1
            array1[i][j] = 1
        else:
            print("Number is incompatable")

array1[array1 %2 == 0] = 0
array1[array1 %2 == 1] = 1

print("Number of zeros: ",count0, "Number of  ones: ", count1)

ones = np.count_nonzero(array1 == 1)
zeros = np.count_nonzero(array1 == 0)

print(ones, zeros)
print(array1)
