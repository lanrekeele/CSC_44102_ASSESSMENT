import os

# This function views all ticket saved in the ticket.txt file.
# It reads from the ticket.xt file line by line and prints the ticket details for each ticket found in the file.
def view_all_tickets():
    filename = "tickets.txt"

    # Lets check if the file exist
    if not os.path.exists(filename):
        print("No tickets found.")
        return

    with open(filename, "r") as file:
        tickets = file.readlines()

    if not tickets:
        print("No tickets found.")
        return
    
    print("\n===== FIND ALL HELP DESK TICKETS BELOW =====")
    
    for ticket in tickets:
        ticket_details = eval(ticket.strip())
        print(eval(ticket.strip()))

#view_tickets()