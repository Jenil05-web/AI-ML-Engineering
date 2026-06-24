import numpy as np

# Scalar Arithmetic

# array = np.array([1,2,3])

# print(array+1)
# print(array-2)
# print(array/4)
# print(array*3)

# Vectorized funcs

# array = np.array([1.0333,2.21,3.99])

# print(np.sqrt(array)) # it will give square root of the function
# print(np.round(array) ) # it will round off the number
# print(np.ceil(array)) # it will always round upp to the upper greatest number 

#Exercise
radii = np.array([1,2,3])

print (np.pi * radii**2) # this is ** means power of 2 

# Element wise arithmetic

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2) # it will simply add and will give us single array
print(array1 - array2)
print(array1 *array2)
print(array1 /array2)
print(array1 ** array2) # it will raise to power of array1

# Comparision Operators

scores = np.array([12, 78 , 89 , 100 , 72])
print(scores == 100) # output [False False False  "True" False]
print(scores >= 100) # similarly ....










 