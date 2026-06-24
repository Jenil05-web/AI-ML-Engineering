import pandas as pd

df = pd.read_csv("data.csv")

# Filtering : keeping rows that match a condition 
rich_customers = df[df["Email"] =="colleen91@faulkner.biz"] # here we added an filter that we want emaisl with this name then we will get the filtered ouput
print(rich_customers) # same we can use other operators also in condition 
print(rich_customers)