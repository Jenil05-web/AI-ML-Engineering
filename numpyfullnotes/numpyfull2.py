import numpy as np

# Slicing 
array1 = np.array([[1,2,3,4],# 0
                  [5,6,7,8],# 1
                  [9,10,11,12], # 2
                  [13,14,15,16]])# 3

# array[start:end:step] #

# print(array1[0:2])
print(array1[0:3:2]) # it will give row 1 and row 2


# Imagine your array is a tray of cookies fresh from the oven. 🍪

# Our Goal: We want to grab a plate with only the cookies in the very middle
# [[ 6,  7],
#  [10, 11]]

# Of course Let's use a very simple, practical example.


# Python

# # Our tray of cookies
# tray = np.array([[ 1,  2,  3,  4],
#                  [ 5,  6,  7,  8],
#                  [ 9, 10, 11, 12],
#                  [13, 14, 15, 16]])
# Our Goal: We want to grab a plate with only the cookies in the very middle:

# [[ 6,  7],
#  [10, 11]]
# To do this, we need to tell Python two things:

# Which rows do we want?

# Which columns do we want?

# We use the format tray[rows, columns].

# ## Step 1: Find the Rows
# First, look at the tray and find the rows that have the cookies we want (6, 7, 10, 11).

# Cookie 6 and 7 are in Row 1.

# Cookie 10 and 11 are in Row 2.

# So, we need rows starting at index 1 and ending before index 3. The slice for this is 1:3.

# ## Step 2: Find the Columns
# Now, just looking at those selected rows, find the columns that have our cookies.

# Cookie 6 and 10 are in Column 1.

# Cookie 7 and 11 are in Column 2.

# So, we need columns starting at index 1 and ending before index 3. The slice for this is also 1:3.

# ## Step 3: Combine Them
# Now we put our row instructions and column instructions together, separated by a comma.

# middle_cookies = tray[1:3 , 1:3]

# Python understands this as:
# "From the tray, first select only rows 1 and 2. Then, from that smaller selection, take only columns 1 and 2."

# When you print middle_cookies, you get exactly the block you wanted:

# [[ 6  7]
#  [10 11]]
# In short, slicing a 2D array is just drawing a box over the numbers you want by specifying the start and end rows, and the start and end columns.
