import pandas as pd

df = pd.read_csv("data.csv")

# Data Cleaning : The process of fixing/removing :
# incomplete  , incorrect  or irrelevant data 

# MOST IMP topic as 75% of the work done with pandas with this topic

# Drop irrelevent columns

df.drop(columns=["Emails"])  # it will delete this column 

# Handle missing data
df = df.dropna(subset=["Company"]) # it will drop any rows which will have missing values 

df = df.fillna({"Company": "None"}) # it will replace missing values with none"

# Fix inconsitent values

df["Emails"] = df["Emails"].replace({"Companies" : "Job"})

