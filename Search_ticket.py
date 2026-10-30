import os
# This function views individual tickets based on the ticket ID provided by the user. 
# It reads from a file named "tickets.txt" and searches for the ticket with the matching ticket ID. 
# If found, it prints the ticket details; otherwise, it informs the user that the ticket was not found.
def search_ticket():
    try:
        ticket_ID = int(input("Please enter the ticket ID you will like to view: "))
    except ValueError:
        print("Invalid ticket ID. Please enter a valid integer.")
        return
    #Name_of_requester = input("Please enter the name of the ticket requester: ")
    if not os.path.exists("tickets.txt"):
        print("No tickets found.")
        return
    with open("./ASSESSMENT/tickets.txt", "r") as file:
        for line in file:
            ticket = eval(line.strip())
            if int(ticket["Ticket Number"]) == ticket_ID:
                print(f"Ticket details: {ticket}")
                return
    print("No Ticket with this Ticket ID exists.")
#search_ticket()