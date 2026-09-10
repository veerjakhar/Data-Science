import numpy as np

array1 = np.array(range(1, 16))
array2 = np.array(range(1, 11))
array3 = np.arange(1, 10).reshape(3, 3)
array4 = np.arange(10, 19).reshape(3, 3)

print(array1)
a = array1[array1 < 8]
b = array1[array1 >= 10]
c = array1[array1 %2 == 1]
print(a)
print(b)
print(array1[::2])
print(c)

print(array2)
d = []
e = []
f = []
'''for i in array2:
    d.append(i + 5)'''
d = array2 + 5
e = array2 * 3
f = array2 - 2
print(d)
print(e)
print(f)

g = []
g = array3 @ array4 # (array3 * array4) (* '=' and '!=' @ (correct way))
print(g)

# Linear equation: y = mx + b
# Quadrtic Question = x^2

m = float(input("Enter the value of 'm': "))
b = float(input("Enter the value of 'b': "))

print("The linear eqution is: y = ", m, "x + ", b)
for x in range(10):
    y = m * x + b
    print(y)




