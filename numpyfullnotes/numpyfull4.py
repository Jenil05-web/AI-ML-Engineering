import numpy as np

# Brodcasting  allows numpy to perform operations on arrays 
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape

# The dimensions have the same size 
# OR
# one of the dimensions has size of 1

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1] , [2] , [3] , [4]])
print(array1.shape)
print(array2.shape)

print(array1 * array2)

# Exercise : Multiplicatoin table

arraym1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
arraym2 = np.array([[1] , [2] , [3] ,[4] , [5] ,[6] , [7] ,[8] , [9] , [10] ])

print(arraym1.shape)
print(arraym2.shape)

print(arraym1* arraym2)