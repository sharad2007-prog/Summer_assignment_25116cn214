print("Welcome to Contact Management System")

contacts = []

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    x = int(input("Enter your choice: "))

    if x == 1:
        contact_id = int(input("Enter Contact ID: "))
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contact = {
            "contact_id": contact_id,
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif x == 2:
        search_id = int(input("Enter Contact ID to search: "))
        found = False

        for contact in contacts:
            if contact["contact_id"] == search_id:
                print("Contact ID:", contact["contact_id"])
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True
                break

        if found == False:
            print("Contact not found!")

    elif x == 3:
        delete_id = int(input("Enter Contact ID to delete: "))
        found = False

        for contact in contacts:
            if contact["contact_id"] == delete_id:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if found == False:
            print("Contact not found!")

    elif x == 4:
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            for contact in contacts:
                print("\nContact ID:", contact["contact_id"])
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    elif x == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
