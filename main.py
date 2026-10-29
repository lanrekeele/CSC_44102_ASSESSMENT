from create_ticket import create_ticket
from view_ticket import view_all_tickets
from Search_ticket import search_ticket
from Update_ticket import update_ticket

def main():
    while True:
        print("\n===== HELP DESK TICKET SYSTEM =====")
        print("1. Create a new ticket")
        print("2. View all tickets")
        print("3. Search for a ticket by ID")
        print("4. Update Existing Ticket")
        print("5. Exit")
        
        choice = input("Please select an option (1-5): ").strip()      
        if choice == '1':
            create_ticket()
        elif choice == '2':
            view_all_tickets()
        elif choice == '3':
            search_ticket()
        elif choice == '4':
            update_ticket()
        elif choice == '5':
            print("Thank You for your time. Goodbye!!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
