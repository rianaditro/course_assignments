import re


contacts = []

def add_contact(name, phone, email):
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)

def remove_contact(index):
    index = index - 1
    if index < len(contacts):
        contacts.pop(index)
    else:
        print("Invalid index")

def update_contact(index, name=None, phone=None, email=None):
    index = index - 1
    if index < len(contacts):
        contact = contacts[index]
        if name:
            contact['name'] = name
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
    else:
        print("Invalid index")

def list_contacts():
    for i, contact in enumerate(contacts):
        print(f"{i+1}: {contact.get('name')}")

def get_contact(index):
    index = index - 1
    if index < len(contacts):
        contact = contacts[index]
        print(f"{index+1}: {contact.get('name')} - {contact.get('phone')} - {contact.get('email')}")
    else:
        print("Invalid index")

def is_valid_index(index) -> dict[str, bool | int | None]:
    try:
        index = int(index)
    except ValueError:
        print("Invalid index")
        return {"valid": False, "index": None}
    
    if index < 1 or index > len(contacts):
        print("Invalid index")
        return {"valid": False, "index": None}
    return {"valid": True, "index": index}

def is_valid_email(email):
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(email_regex.match(email))

def is_valid_phone(phone):
    phone_regex = re.compile(r'^\+?1?\d{9,15}$')
    return bool(phone_regex.match(phone))

def search_contacts(query):
    results = []
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query.lower() in contact['phone'].lower() or query.lower() in contact['email'].lower():
            results.append(contact)
    return results


while True:
        print("\nContact Manager")
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Update contact")
        print("4. List contacts")
        print("5. Get contact")
        print("6. Search contacts")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            if is_valid_phone(phone) and is_valid_email(email):
                add_contact(name, phone, email)
            else:
                print("Invalid phone or email")
        elif choice == "2":
            index = input("Enter index to remove: ")
            valid_index = is_valid_index(index)
            if valid_index.get("valid"):
                remove_contact(valid_index.get("index"))
        elif choice == "3":
            index = input("Enter index to update: ")
            valid_index = is_valid_index(index)
            if valid_index.get("valid"):
                name = input("Enter new name (leave blank to keep unchanged): ")
                phone = input("Enter new phone (leave blank to keep unchanged): ")
                email = input("Enter new email (leave blank to keep unchanged): ")
                update_contact(valid_index.get("index"), name, phone, email)
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            index = input("Enter index to gezt: ")
            valid_index = is_valid_index(index)
            if valid_index.get("valid"):
                get_contact(valid_index.get("index"))
        elif choice == "6":
            query = input("Enter search query: ")
            results = search_contacts(query)
            if len(results) > 0:
                print("\nSearch Results:")
                for i, contact in enumerate(results):
                    print(f"{i+1}: {contact.get('name')} - {contact.get('phone')} - {contact.get('email')}")
            else:
                print("No contacts found")
        elif choice == "7":
            break
        else:
            print("Invalid choice")