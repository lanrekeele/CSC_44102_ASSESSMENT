import json
import os
import random as rn

TICKETS_FILE = "ticket.json"


def load_tickets(filepath=TICKETS_FILE):
    """Load existing tickets from the JSON file safely."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as record:
            return json.load(record)
    except json.JSONDecodeError:
        # File is empty or malformed; fall back to empty list
        return []


def generate_unique_ticket_id(existing_tickets):
    """Generate a random 4-digit ID that doesn't collide with existing tickets."""
    existing_ids = {ticket.get("Ticket Number") for ticket in existing_tickets}
    ticket_number = rn.randint(1000, 9999)
    while ticket_number in existing_ids:
        ticket_number = rn.randint(1000, 9999)
    return ticket_number


def create_ticket():
    # 1. Load existing records first
    all_user_tickets = load_tickets()

    # 2. Gather user input
    name = input("Please enter the name of ticket requester: ").strip()
    dept = input("Please enter the department of ticket requester: ").strip()
    phone_number = input("Enter phone number details of requesting user: ").strip()
    user_email = input("Enter email address of requesting user: ").strip()
    issue = input("Please describe the issue you are experiencing: ").strip()
    priority = input("Please enter ticket priority (Low/Medium/High): ").strip().capitalize()

    # 3. Generate a guaranteed non-colliding ticket number
    ticket_number = generate_unique_ticket_id(all_user_tickets)

    # 4. Assemble ticket object
    user_ticket = {
        "Ticket Number": ticket_number,
        "Name": name,
        "Department": dept,
        "Phone Number": phone_number,
        "Email Address": user_email,
        "Issue": issue,
        "Priority": priority,
    }

    # 5. Append and persist back to file
    all_user_tickets.append(user_ticket)
    with open(TICKETS_FILE, "a", encoding="utf-8") as record:
        json.dump(all_user_tickets, record, indent=4)

    print(f"\nTicket created successfully! Your ticket number is: {ticket_number}")
    return user_ticket


if __name__ == "__main__":
    new_ticket = create_ticket()
    print("\nReturned ticket record:")
    print(new_ticket)