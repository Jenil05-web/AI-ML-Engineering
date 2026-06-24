import pandas as pd

# Series = A pandas 1-Dimensional labeled array that can hold any data type 
# think of it like a single column in excel 

data = [100,102,104]

series = pd.Series(data , index=["A" , "B" , "C" ]) # .series in an object / method 

print(series)
print(series.loc["A"]) #  .loc (location by label) it will give us location of the index and the number which it posses

# .iloc method will give us integer location 

# we can also set series index we can add index numbers 

calories = {"day1" : 1200 , "day2": 3000 , "day3": 2341 , "day4": 3793}

series = pd.Series(calories)

print(series)
print(series[series>=2000])

