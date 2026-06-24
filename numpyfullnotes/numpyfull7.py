import numpy as np

# Random numbers  IMP

rng = np.random.default_rng()

print(rng.integers(low=1,high = 7 , size=(2,3))) # 1,7 is range means it will give us numbers from 1 to 6


array = np.array([1,2,3,4,5,6,7,8,9,10])

rng.shuffle(array) # it will shuffle our array 
rng.choice(array)

print(array ) 