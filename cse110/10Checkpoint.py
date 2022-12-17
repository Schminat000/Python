print("Please enter the items of the shopping list (type: quit to finish):")

shopping_cart = []
item = None

while item != "quit":
    item = input('Item: ')
    if item != "quit":
        shopping_cart.append(item)
print("\nThe shopping cart is:")
for item in shopping_cart:
    print(item)
print("\nThe shopping list with indexes is:")
for i in range(len(shopping_cart)):
    item = shopping_cart[i]
    print(f"{i}. {item}")
index = int(input("\nWhich item would you like to change? "))
new_item = input("\nWhat is the new item? ")
shopping_cart[index] = new_item
print("\nThe shopping list with indexes is:")
for i in range(len(shopping_cart)):
    item = shopping_cart[i]
    print(f"{i}. {item}")

# 10Checkpoint.py