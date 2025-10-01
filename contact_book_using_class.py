# Contact Book
""" This project is a contact book that stores user details(name,phonenumber,email) using dictionaries in python.
It allows a user to add/delete/update/search a contact. Used : OOPS, Dictionary, Functions, Control and conditional statements. """

def print_star():
    """To print star"""

    print("********************")


def menu():
    """To print the menu of contact book"""

    print("--- Contact Book ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Show Contact")
    print("6. Exit")


def contact_details():
    """To input values from user for the contact book (name,ph number and email)"""

    name = input("\nEnter the name:")     
    phoneNumber = int(input("Enter the phone number:"))
    emailId = input("Enter the email id:")
    return name, phoneNumber, emailId


def add_contact(contact):
    """To add a contact to contact book"""

    name, phoneNumber, emailId = contact_details()
    if name in contact:
        print(f"\n{name} already exist in the contact book\n")
    else:    
        contact[name] = {"Phonenumber":phoneNumber,"EmailID":emailId}
        print("\nContact added successfully\n")


def delete_contact(contact):
    """To delete a contact from contact book"""

    name = input("\nEnter the name of the person to delete:")
    if name in contact:
        del contact[name]
        print("\nSuccessfully Deleted Contact\n")
    else:
        print(f"\n{name} not exist in the contact book!!!\n")


def update_contact(contact):
    """To update a contact in the contact book"""

    name = input("\nEnter the name to update the contact:")
    if name in contact:
        new_name = input("\nNew name (or press Enter to keep this name):")
        new_phone = input("New phone (or press Enter to keep this phonenumber):")
        new_email = input("New email (or press Enter to keep this email):")

        target = contact[name]   # to create an alias for storing values from dictionary contact
        if new_phone:
            target['phone'] = new_phone
        if new_email:
            target['email'] = new_email
        if new_name and new_name != name:
            contact[new_name] = contact.pop(name)
            print(f"\nContact renamed to {new_name} and updated.\n")
        else:
            print(f"\nContact {name} updated.\n")

    else:
        print(f"\n{name} not exist in the contact book!!!\n")


def print_contact_details(name, details):
    """To print the contact details"""

    print(f"\nName:        {name}")
    print(f"Phonenumber: {details.get('Phonenumber')}")
    print(f"EmailID:     {details.get('EmailID')}\n")


def search_contact(contact):
    """To search a contact is available in the contact book"""

    name = input("\nEnter the name to search in your contact book:")
    if name in contact:
        print(f"\n{name} is in contact book\n")
        decision = input("Do you want to see the details(y/n):")  # to ask the user wheather to see the details
        if decision.lower() == 'y':
            print_contact_details(name, contact[name])
    else:
        print(f"\n{name} not found in your contact!!!")
        add_new = input("\nDo you want to add this contact?(y/n):")  # if no contact found, asking user to add that name to contact
        if add_new.lower() == 'y':
            add_contact(contact)


def display_contact(contact):
    """To display the contacts in the contact book"""

    if not contact:
        print("\nNo contacts to show\n")
        return
    
    print("\n----All contacts----")
    print_star()
    for name, details in contact.items():
        print_contact_details(name, details)


contact = {}

while True:

    print_star()
    menu()
    print_star()

    choice = int(input("Choose a option (1 - 6) to continue:"))

    if choice == 1:
        add_contact(contact)

    elif choice == 2:
        delete_contact(contact)

    elif choice == 3:
        update_contact(contact)
        
    elif choice == 4: 
        search_contact(contact)
    
    elif choice == 5:
        display_contact(contact)
    
    elif choice == 6:
        print("\nExiting the Contact Book, Bye:)\n")
        exit()

    else:
        print("\nEnter a valid option from the menu!!!\n")