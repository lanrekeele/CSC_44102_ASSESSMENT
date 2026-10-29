import random as rn
#A function to create a new ticket for the helpdesk system. 
# It prompts the user for their name, department, issue, and priority, generates a random ticket number, 
# and stores all this information in a dictionary. 
# The function then prints the ticket details and returns the dictionary.
all_user_tickets = []
def create_ticket():
    #Create a fresh and empty dictionary to hold all ticket and equest information
    user_ticket = {}
    name = input("Please enter the name of ticket requester: ")
    dept = input("Please enter the department of ticket requester: ")
    issue = input("Please describe the issue you are experiencing: ")
    priority = input("Please enter the priority of ticket: ")
    ticket_number = rn.randint(1000, 9999)
    while any(ticket["Ticket Number"] == ticket_number
              for ticket in all_user_tickets):
        ticket_number = rn.randint(1000, 9999)
    user_ticket["Name"] = name
    user_ticket["Department"] = dept
    user_ticket["Issue"] = issue
    user_ticket["Priority"] = priority
    user_ticket["Ticket Number"] = ticket_number
    print(f"Ticket created successfully! Your ticket number is: {ticket_number}")
    all_user_tickets.append(user_ticket)
    with open("./ASSESSMENT/tickets.txt", "a") as file:
        file.write(f"{user_ticket}\n")
    #print(all_user_tickets)
    #print(f"Ticket details: {user_ticket}")
    return user_ticket
#create_ticket()


#print(f"All tickets: {all_user_tickets}")
