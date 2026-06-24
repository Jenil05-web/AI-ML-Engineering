import pandas as pd

# Importing Imp

df = pd.read_csv("data.csv")

# print(df) it will print first 5 and last 5 rows 

# print(df.to_string()) # it will  print the whole file

# Selection by column

# print(df["First Name"].to_string()) # So it will print the first name of the customers frmo csv file 

customers = input("Enter first name :")

try :
    print(df.loc["Fred"])

except KeyError:
    print(f"Customer no found{customers} ")






