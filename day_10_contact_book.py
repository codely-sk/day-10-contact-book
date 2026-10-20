
contacts = {}


def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()

    if name == "" or phone == "":
        print("Name and phone number cannot be empty!")
        return

    contacts[name] = phone
    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return

    print("\n===== YOUR CONTACTS =====")

    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def search_contact():
    name = input("Enter name to search: ").strip().lower()

    for saved_name, phone in contacts.items():
        if saved_name.lower() == name:
            print(f"Contact found: {saved_name} - {phone}")
            return

    print("Contact not found!")


def update_contact():
    name = input("Enter the contact name to update: ").strip()

    for saved_name in contacts:
        if saved_name.lower() == name.lower():
            new_phone = input("Enter new phone number: ").strip()

            if new_phone == "":
                print("Phone number cannot be empty!")
                return

            contacts[saved_name] = new_phone
            print("Phone number updated successfully!")
            return

    print("Contact not found!")


def delete_contact():
    name = input("Enter the contact name to delete: ").strip()

    for saved_name in contacts:
        if saved_name.lower() == name.lower():
            del contacts[saved_name]
            print("Contact deleted successfully!")
            return

    print("Contact not found!")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please select 1-6.")
