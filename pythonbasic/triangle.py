rows = int(input("Enter no. of rows: "))
columns = int(input("Enter no of columns : "))
symbol = input("Enter a symbol to use: ")

# This is the "outer" loop for the rows
for x in range(rows):
    
    # This is the "inner" loop for the columns
    for y in range(columns):
        # This code is INSIDE the inner loop
        print(symbol, end="")
        
    # This code is OUTSIDE the inner loop, but still inside the outer loop
    print()