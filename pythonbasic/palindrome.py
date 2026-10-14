"""Palindrome simply means the words would remain same even if spelled backwards. for example : madam , 121 etc..."""

item = input("Enter a item :")
item_reversed = item [::-1] # Core logic for reversing the string .
if item_reversed == item :
    print("It is an palindrome item")

else:
    print("It is not an palindrome item")


    """ [::-1] , this is the core logic for reversing the string."""

    