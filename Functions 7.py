def add_item(cart, item_name, quantity, price_per_unit):
    cart.append({"name": item_name, "quantity": quantity, "price_per_unit": price_per_unit})
def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["quantity"] * item["price_per_unit"]
    return total
def display_cart(cart):
    print("\nShopping Cart:")
    for item in cart:
        print(f"{item['name']} - Quantity: {item['quantity']}, Price/Unit: {item['price_per_unit']}")
    print()
def main():
    cart = [] 
    while True:
        print("\n1. Add Item")
        print("2. View Cart")
        print("3. Calculate Total")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price_per_unit = float(input("Enter price per unit: "))
            add_item(cart, item_name, quantity, price_per_unit)
        elif choice == "2":
            display_cart(cart)
        elif choice == "3":
            total = calculate_total(cart)
            print(f"\nTotal Price: ${total:.2f}")
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()