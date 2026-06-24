import numpy as np

# array = np.array([1,2,3,4,5]) # by this way we create arrays 

# array = array*2 # it will double the numbers in array

# print(array)

array = np.array([[['A','B','C'] ,['D','E','F'] ,['G','H','I']],
                  [['J','K','L'] ,['M','N','O'] ,['P','Q','R']], # this is an 3D array
                  [['S','T','U'] ,['V','W','X'] ,['Y','Z','']] ])  

print(array[0,0,2]  ) # this will give 'A'

# [[ depth , row , column ]]

# similarly print(array[0,0,1] ) it will give 'B' , print(array[0,0,1] ) it will give 'C' like that 

# array[0,1,0] will give D
# array[1,1,1] will give N  


# This is Page 0
# [['A','B','C'],
#  ['D','E','F'],
#  ['G','H','I']]

# # This is Page 1
# [['J','K','L'],
#  ['M','N','O'],
#  ['P','Q','R']]

# This is Page 2
# [['S','T','U'],
#  ['V','W','X'],
#  ['Y','Z','']]

#Remember, indexing in programming always starts from 0.

# Example 1: How to get 'A'?
# You already figured this one out! array[0, 0, 0]

# Go to Page 0.

# In that page, go to Row 0.

# In that row, get the element at Column 0.

# Result: 'A'

# Example 2: How to get 'O'?
# Let's find its address.

# 'O' is in the second big block, so that's Page 1.

# Inside that page, it's in the second list, which is Row 1.

# Inside that row, it's the third letter, which is at Column 2.

# So, the address is array[1, 1, 2].

# Example 3: How to get 'W'?

# It's in the third block -> Page 2.

# It's in the second row -> Row 1.

# It's the second character -> Column 1.

# The address is array[2, 1, 1].

# ## Accessing Entire Sections (Slicing)
# Now, what if you want a whole row or even a whole page? You use a colon :, which means "give me everything in this dimension."

# 1. To get an entire page:
# If you want all of Page 1 (the matrix with 'J' through 'R'), you just specify the page number.

# array[1]

# This gives you:

# [['J', 'K', 'L'],
#  ['M', 'N', 'O'],
#  ['P', 'Q', 'R']]
# 2. To get an entire row from a specific page:
# Let's get the row ['P', 'Q', 'R'].

# We know it's on Page 1.

# It's the third row, so that's Row 2.

# We want all columns in that row.

# array[1, 2] or array[1, 2, :]

# This gives you:

# ['P', 'Q', 'R']





