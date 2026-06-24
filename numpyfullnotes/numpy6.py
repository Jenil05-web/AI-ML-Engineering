import numpy as np

# Filtering : refers to the process of selecting elements from an array that match a given condition

ages = np.array([[21,22,44,12,49,11,10] , [93,23,58,73,28,74,73]])

teenagers = ages[ages<18]
adults = ages[(ages>=18) & {ages<60}]
print(adults)
print(teenagers)