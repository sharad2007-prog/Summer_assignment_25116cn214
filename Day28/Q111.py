print("Welcome to Ticket Booking System")

tickets = []

while True:
    print("\n1. Book Ticket")
    print("2. Search Ticket")
    print("3. Cancel Ticket")
    print("4. Display All Tickets")
    print("5. Exit")

    x = int(input("Enter your choice: "))

    if x == 1:
        ticket_id = int(input("Enter Ticket ID: "))
        name = input("Enter Passenger Name: ")
        destination = input("Enter Destination: ")
        seat_no = input("Enter Seat Number: ")
        price = float(input("Enter Ticket Price: "))

        ticket = {
            "ticket_id": ticket_id,
            "name": name,
            "destination": destination,
            "seat_no": seat_no,
            "price": price
        }

        tickets.append(ticket)
        print("Ticket booked successfully!")

    elif x == 2:
        search_id = int(input("Enter Ticket ID to search: "))
        found = False

        for ticket in tickets:
            if ticket["ticket_id"] == search_id:
                print("Ticket ID:", ticket["ticket_id"])
                print("Passenger Name:", ticket["name"])
                print("Destination:", ticket["destination"])
                print("Seat Number:", ticket["seat_no"])
                print("Ticket Price:", ticket["price"])
                found = True
                break

        if found == False:
            print("Ticket not found!")

    elif x == 3:
        cancel_id = int(input("Enter Ticket ID to cancel: "))
        found = False

        for ticket in tickets:
            if ticket["ticket_id"] == cancel_id:
                tickets.remove(ticket)
                print("Ticket cancelled successfully!")
                found = True
                break

        if found == False:
            print("Ticket not found!")

    elif x == 4:
        if len(tickets) == 0:
            print("No tickets booked.")
        else:
            for ticket in tickets:
                print("\nTicket ID:", ticket["ticket_id"])
                print("Passenger Name:", ticket["name"])
                print("Destination:", ticket["destination"])
                print("Seat Number:", ticket["seat_no"])
                print("Ticket Price:", ticket["price"])

    elif x == 5:
        print("Thank you for using the Ticket Booking System!")
        break

    else:
        print("Invalid choice!")
