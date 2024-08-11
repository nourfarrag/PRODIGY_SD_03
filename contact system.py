import json
import os

FILE_NAME = 'contacts.json'

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    if contacts:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts available.")

def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ")
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email address: ")
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            del contacts[i]
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
