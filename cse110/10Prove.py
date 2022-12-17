# This is a welcome sign!
print("Welcome to the Shopping Cart Program!")

# This creates our list variables.
shopping_cart = []
cart = None
shopping_cart_price = []

# This is the coding to do the milestone requirements.
while cart != "5":
    print("\nPlease select one of the following:\n1. Add item\n2. View cart\n3. Change item\n4. Compute total\n5. Quit")
    cart = input("Please enter an action: ")

# Option One adds the item and price to their respective lists.
    if cart == "1":
        new_item = input("What item would you like to add? ")
        new_item_price = float(input(f"What is the price of '{new_item}'? $"))
        shopping_cart.append(new_item)
        shopping_cart_price.append(new_item_price)
        print(f"'{new_item}' has been added to the cart.")

# Option Two displays the item and it's price.
    if cart == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_cart)):
            print(f"{i + 1}. {shopping_cart[i]} - ${shopping_cart_price[i]:.2f}")

# Option Three gives the chance for the user to remove and/or replace the item of their choice.
    if cart == "3":
        index = int(input("\nWhich item would you like to remove? "))
        index += -1
        if index < len(shopping_cart):
            shopping_cart.pop(index)
            shopping_cart_price.pop(index)
            option = input("Would you like to replace the item (yes or no)? ")
            if option.upper() == "YES":
                new_item = input("\nWhat is the new item? ")
                shopping_cart.append(new_item)
                changed_price = float(input(f"What is the price of '{new_item}'? $"))
                shopping_cart_price.append(changed_price)
                print(f"'{new_item}' has been added to the cart.")
            elif option.upper() == "NO":
                print("Item removed.")
        else:
            print("Sorry, that is not a valid item. Please try again.")

# Option Four displays the cart's sum.
    if cart == "4":
        total = sum(shopping_cart_price)
        print(f"The total price of the items in the shopping cart is: ${total:.2f}")

# Option Five exits the program and says thank you!
    if cart == "5":
        print("Thank you. Goodbye.")

# python 10Prove.py