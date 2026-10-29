import os
import ast
#This module ensures that ticket details can be updated. An instance will be if the support specialist picks up a ticket, He or she can update and make changes
#to thet ticket and submit it and the updated information will be written to the ticket.txt file

def update_ticket():
    try:
        ticket_ID = int(
            input("Please enter the ticket ID you want to update: ")
        )
    except ValueError:
        print("Invalid ticket ID. Please enter a valid integer.")
        return

    if not os.path.exists("./ASSESSMENT/tickets.txt"):
        print("No tickets found.")
        return

    all_tickets = []

    #Read all tickets
    with open("./ASSESSMENT/tickets.txt", "r") as file:
        for line in file:
            if line.strip():
                ticket = ast.literal_eval(line.strip())
                all_tickets.append(ticket)

    #  Search for the ticket
    ticket_found = False

    for ticket in all_tickets:
        if ticket["Ticket Number"] == ticket_ID:
            print(f"Ticket Details to be edited or updated are: {ticket}")
            status = input("Enter the status of the ticket: ")
            response = input("Enter an updated response: ")
            # Update the dictionary.
            ticket["Ticket_Status"] = status
            ticket["Ticket_Response"] = response
            # Set ticket_found to True.
            ticket_found = True
            pass

    #  Save the tickets if a match was found
    if ticket_found:
        with open("./ASSESSMENT/tickets.txt", "w") as file:
            for ticket in all_tickets:
                file.write(str(ticket) + "\n")

        print("Ticket updated successfully.")
    else:
        print(f"Ticket ID {ticket_ID} was not found.")

#
# if __name__ == "__main__":
    # update_ticket()