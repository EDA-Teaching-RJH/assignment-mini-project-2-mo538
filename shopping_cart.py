import sys
import re
import csv

# Store class for managing the items and their prices.
class Store:
    def __init__(self):
        #Define the available items and their selling prices.
        self.items = {
            "Hoodie set": 15.99,
            "Jumper": 16.99,
            "Shoes": 19.99,
            "Winter Coat": 39.99,
            "Beanie": 5.99
        }

    # this a way for displaying available items  and their prices.
    def display_items(self):
        print("\nAvailable Items:")
        for item, price in self.items.items():
            print(f"- {item}: £{price:.2f}")

# this class also manages the users cart items
class Cart:
    def __init__(self):
        #Create an empty cart
        self.cart = {}

    # this is a way of adding an item to the cart with a specified amount.
    def add_item(self, item, quantity, items_in_store):
        # this then checks if we have the item available in the store 
        if item in items_in_store:
            # Add  an item to the cart, or increasing the amount if item is  already in the cart.
            self.cart[item] = self.cart.get(item, 0) + quantity
            print(f"Added {quantity}x {item}(s) to your cart.")
        else:
            print("Item not found. Please choose from the available list.")

    # a way of viewing the current item and its total cost
    def view_cart(self, items_in_store):
        if not self.cart:
            print("\nYour cart is empty.")
            return

        total = 0
        print("\nYour Cart:")
        # shows  each item in the cart with quantity and price
        for item, quantity in self.cart.items():
            price = items_in_store[item] * quantity
            total += price
            print(f"- {item}: {quantity}x @ £{items_in_store[item]:.2f} each = £{price:.2f}")
        print(f"Total: £{total:.2f}")

    # a way to proceed with the checkout and clear the cart if successful
    def checkout(self, items_in_store):
        if not self.cart:
            print("\nYour cart is empty.Make sure to  add items before checking out.")
            return

        self.view_cart(items_in_store)
        if input("\nContinue to checkout? (yes/no): ").strip().lower() == "yes":
            print("\nThank you for shopping with Bukola store! Your order has been placed, you should get a confirmation email.")#confirmation email
            self.cart.clear()  # Clear the cart after each checkout
        else:
            print("\nCheckout cancelled.")

    # a way to save the current cart to a CSV file
    def save_cart(self, filename="cart.csv"):
        if not self.cart:
            print("Your cart is currently empty. There is no item  to save.")
            return
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Item', 'Quantity'])
            # Add each item and its amount from the cart to the CSV file.
            for item, quantity in self.cart.items():
                writer.writerow([item, quantity])
        print(f"Your cart has now been saved to {filename}.")

    # a way to load a saved cart from the saved csv file
    def load_cart(self, filename="cart.csv", items_in_store=None):
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  
                # this then loads items and amounts from the CSV file to the cart.
                for row in reader:
                    item, quantity = row
                    if items_in_store and item in items_in_store:
                        self.cart[item] = int(quantity)
        except FileNotFoundError:
            print(f"No saved cart was found. Begin with an empty cart.")

# The InputValidator class in this case validates the user inputs (e.g., quantity).
class InputValidator:
    @staticmethod
    def is_valid_quantity(quantity):
        # Check whether the quantity is a positive integer.
        return bool(re.match(r'^[1-9][0-9]*$', quantity))

# this function displays the menu choices to the user.
def display_menu():
    print("\nWelcome to Bukola Clothing Store!")
    print("1. View Clothing Items")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Save Cart")
    print("6. Load Cart")
    print("7. Exit")

# The main function is to control the store operations.
def main():
    store = Store()  
    cart = Cart()  
    validator = InputValidator()  

    cart.load_cart()  # Try to load the cart from file.

    while True:
        display_menu()  # Show all the menu options
        choice = input("Enter your choice: ").strip()  # Get input from the user for menu selection.

        if choice == "1":
            store.display_items()  # Display the items available
        elif choice == "2":
            store.display_items()  # Display the available  items again before adding to cart
            item = input("Enter the name of the item you want to add: ").strip()
            quantity = input("Enter quantity: ").strip()

            if not validator.is_valid_quantity(quantity):
                print("Invalid quantity. Please enter a positive number.")
                continue

            cart.add_item(item, int(quantity), store.items)  # Add the item to the cart
        elif choice == "3":
            cart.view_cart(store.items)  # View the items in the cart
        elif choice == "4":
            cart.checkout(store.items)  # Proceed to checkout the items
        elif choice == "5":
            cart.save_cart()  # we can save the current cart to a file
        elif choice == "6":
            cart.load_cart()  # and also load the cart from a file
        elif choice == "7":
            print("Thank you for visiting Bukola Clothing Store! Goodbye.")
            sys.exit()  # Exit the program
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Run the main function when the script finishes being executed.
if __name__ == "__main__":
    main()
