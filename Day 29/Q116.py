inventory = []

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))

        product = {
            "id": pid,
            "name": name,
            "quantity": quantity,
            "price": price
        }

        inventory.append(product)
        print("Product added successfully.")

    elif choice == 2:
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            for product in inventory:
                print("ID:", product["id"])
                print("Name:", product["name"])
                print("Quantity:", product["quantity"])
                print("Price:", product["price"])
                print("---------------------------")

    elif choice == 3:
        search_id = int(input("Enter Product ID to search: "))
        found = False

        for product in inventory:
            if product["id"] == search_id:
                print("ID:", product["id"])
                print("Name:", product["name"])
                print("Quantity:", product["quantity"])
                print("Price:", product["price"])
                found = True
                break

        if not found:
            print("Product not found.")

    elif choice == 4:
        delete_id = int(input("Enter Product ID to delete: "))
        found = False

        for product in inventory:
            if product["id"] == delete_id:
                inventory.remove(product)
                found = True
                print("Product deleted successfully.")
                break

        if not found:
            print("Product not found.")

    elif choice == 5:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid Choice!")
