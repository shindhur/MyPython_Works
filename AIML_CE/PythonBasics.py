import numpy as np

print("Hello Python")
array_1d = np.array([2, 8, 4, 9, 1])
print(array_1d)
input_list = [[5, 6, 7], [7, 6, 5], [0, 8, 7]]
list_1 = np.array([2, 8, 4, 9, 1])
list_2 = np.array([5, 1, 10, 7, 15])

array_1 = np.array([list_1, list_2])
array_2d = np.array(input_list)

print(array_2d[0:, 1])
print(np.shape(array_1))
print(np.ndim(array_1))
#array_2d = np.array([list_1], [list_2])
#print(array_2d)

# Reshaping Arrays ------
some_array = np.arange(0, 12).reshape(3, 4)
print(some_array)
some_array.reshape(2, 6)
print(some_array.reshape(2, 6))
print(some_array.reshape(4, -1))
print(some_array.T)

# Stacking and Splitting Arrays

# Linear Algebra Operartions

list_1 = input_list[0]
list_2 = input_list[1]
list_3 = input_list[2]
array_1 = np.array([list_1, list_2, list_3])
eigen = np.linalg.eig(array_1)
inv = np.linalg.inv(array_1)
det = np.linalg.det(array_1)
print(eigen)
print(inv)
print(det)