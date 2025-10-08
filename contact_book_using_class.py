# Contact Book
""" A simple Contact Book application built in Python to manage user details such as name, phonenumber and email. This project demonstrates two different programming approaches functional programming and object-oriented programming(OOP) to get a clear understanding of both styles.

Features:
Show All Contacts – View all saved contacts.
Add Contact – Save a new contact with name, phone number and email.
Delete Contact – Remove an existing contact by name.
Update Contact – Modify contact details (name, phone number or email).
Search Contact – Find and display specific contact information.

Concepts Covered:
Python Dictionaries
Functions and Control Flow
Object-Oriented Programming (Class, Methods, Objects) """

class Contactbook:

    def __init__(self):
        self.contact = {}
    

    def contact_details(self):
        """To input values from user for the contact book (name,ph number and email)"""

        name = input("\nEnter the name:")     
        phoneNumber = int(input("Enter the phone number:"))
        emailId = input("Enter the email id:")
        return name, phoneNumber, emailId


    def add_contact(self):
        """To add a contact to contact book"""

        name, phoneNumber, emailId = self.contact_details()
        if name in self.contact:
            print(f"\n{name} already exist in the contact book")
        else:    
            self.contact[name] = {"Phonenumber":phoneNumber,"EmailID":emailId}
            print(f"\nContact {name} added successfully!!!")


    def delete_contact(self):
        """To delete a contact from contact book"""

        name = input("\nEnter the name of the person to delete:")
        if name in self.contact:
            del self.contact[name]
            print(f"\nContact {name} deleted successfully!!!")
        else:
            print(f"\n{name} not exist in the contact book.")


    def update_contact(self):
        """To update a contact in the contact book"""

        name = input("\nEnter the name to update the contact:")
        if name in self.contact:
            new_name = input("\nNew name (or press Enter to keep this name):")
            new_phone = input("New phone (or press Enter to keep this phonenumber):")
            new_email = input("New email (or press Enter to keep this email):")

            target = self.contact[name]   # to create an alias for storing values from dictionary contact
            if new_phone:
                target['Phonenumber'] = new_phone
            if new_email:
                target['EmailID'] = new_email
            if new_name and new_name != name:
                self.contact[new_name] = self.contact.pop(name)
                print(f"\nContact renamed to {new_name} and updated.")
            else:
                print(f"\nContact {name} updated.")

        else:
            print(f"\n{name} not exist in the contact book!!!")


    def print_contact_details(self, name, details):
        """To print the contact details"""

        print(f"\nName:        {name}")
        print(f"Phonenumber: {details.get('Phonenumber')}")
        print(f"EmailID:     {details.get('EmailID')}")


    def search_contact(self):
        """To search a contact is available in the contact book"""

        name = input("\nEnter the name to search in your contact book:")
        if name in self.contact:
            print(f"\n{name} is in contact book\n")
            decision = input("Do you want to see the details(y/n):")  # to ask the user wheather to see the details
            if decision.lower() == 'y':
                self.print_contact_details(name, self.contact[name])
        else:
            print(f"\n{name} not found in your contact!!!")
            add_new = input("\nDo you want to add this contact?(y/n):")  # if no contact found, asking user to add that name to contact
            if add_new.lower() == 'y':
                self.add_contact()


    def show_contact(self):
        """To display the contacts in the contact book"""

        if not self.contact:
            print("\nNo contacts to show!!!")
            return
        
        print("\n----All contacts----")
        self.print_star()
        for name, details in self.contact.items():
            self.print_contact_details(name, details)


    def print_star(self):
        """To print star"""

        print("********************")

contactbook = Contactbook()

while True:

    print("\n")
    contactbook.print_star()
    print("--- Contact Book ---")
    print("1. Show Contacts")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Search Contact")
    print("6. Exit")
    contactbook.print_star()

    choice = int(input("Choose a option (1 - 6) to continue:"))

    if choice == 1:
        contactbook.show_contact()

    elif choice == 2:
        contactbook.add_contact()

    elif choice == 3:
        contactbook.delete_contact()
        
    elif choice == 4: 
        contactbook.update_contact()
    
    elif choice == 5:
        contactbook.search_contact()
    
    elif choice == 6:
        print("\nExiting the Contact Book, Bye:)\n")
        exit()

    else:
        print("\nEnter a valid option from the menu!!!\n")