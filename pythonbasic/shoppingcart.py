cart = []

while len(cart)<=5:
    item = input("Add an item : ")
    cart.append(item)
    print(f"Your cart has {cart}")
    
print("---")
print("Your cart is full ! you can only add 5 items in cart")
print(f"final items :{cart}")