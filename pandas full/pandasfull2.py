import pandas as pd

# Dataframe = A tabular data structre with rows AND columns (2 dimensional)
# Similar to Execel spreadsheet

data = {"Name":["ironman" , "Spongebob" , "capAmerica"],
         "Age" : [30,23,48]
         }

df = pd.DataFrame(data)
df = pd.DataFrame(data , index=["hero1" , "hero2" , "hero3"])
print(df.loc["hero1"]) # to select specific data o
print(df)

# Add an new column

df["Act"] = ["Cook" , "NA" , "cashier"] # we can add an new columns by this way 
print(df)

# Add a new row

new_row = pd.DataFrame([{"Name" : "sandy"} , {"Age":23} , {"Hero4": "spiderman"}])

df = pd.concat([df , new_row])

print(df)