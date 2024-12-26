def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts.append({"name": name, "phone": phone})
    print(f"Contact '{name}' added successfully.\n")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.\n")
        return
    print("Contacts List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")
    print()  # Add a new line for better readability

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed_contact = contacts.pop(index)
            print(f"Contact '{removed_contact['name']}' deleted successfully.\n")
        else:
            print("Invalid contact number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main_menu():
    contacts = []
    
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main_menu()

# Author - Mmabiaa
