import pandas as pd

# aggregrate functions = Reduces a set of values into single summary value
# Used to summarize and analyze data
# Often used with tye groupby() function

df = pd.read_csv("data.csv")
print(df.mean(numeric_only=True))
 # it will return only numeric value from csv file
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))


# Single Columns

# print(df["Emails"].sum())
# print(df["Emails"].min())
# print(df["Emails"].max())

# print(group["Emails"].mean()) it will group the datat which is 