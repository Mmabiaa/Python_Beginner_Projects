contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

while True:
    name = input("Enter contact name (or 'quit' to exit): ")
    
    if name.lower() == 'quit':
        break
    
    phone = input(f"Enter phone number for {name}: ")
    add_contact(name, phone)

print(contacts)
